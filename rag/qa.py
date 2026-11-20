from openai import OpenAI
from rag.config import OPENAI_API_KEY, CHAT_MODEL
from rag.vector_store import search_documents

SYSTEM_PROMPT = """You are NaviCare, an informational navigator for Singapore's CareShield Life and ElderShield schemes.
Use ONLY the retrieved policy passages to state policy facts. Do not invent eligibility rules, premiums, payouts, dates, incentives, subsidies or legal interpretations. If retrieved passages do not answer a question, say what is missing and direct the user to the relevant official agency. Distinguish confirmed facts from general explanations. Never make a final insurance, medical, financial or eligibility determination. Do not diagnose disability. Explain that only an MOH-accredited severe disability assessor can determine the assessment outcome. For premiums, direct users to the CPF Board personalised Premium Checker; do not calculate personalised premiums from incomplete profile data. For claims, explain published processes but do not promise claim approval.
Use clear, empathetic plain language. Cite every material policy statement inline in the format [Source: filename, page number if available — URL]. If no source URL is available, cite the filename. If sources conflict or have different dates, flag the conflict and prefer the latest applicable official source while explaining the date.
"""


def answer_question(question: str, profile: dict | None = None, k: int = 5):
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is missing.")
    # Add self-reported profile attributes to the semantic query so cohort- and
    # coverage-specific policy passages are more likely to be retrieved.
    profile_query = " ".join(str(v) for v in (profile or {}).values() if v not in (None, "", "Not provided"))
    retrieval_query = f"{profile_query} {question}".strip()
    matches = search_documents(retrieval_query, k=k)
    context_parts, citations = [], []
    for doc, score in matches:
        meta = doc.metadata
        context_parts.append(
            f"DOCUMENT: {meta.get('source')}\n"
            f"URL: {meta.get('source_url', '')}\n"
            f"PAGE: {meta.get('page', 'not available')}\n"
            f"RELEVANCE: {score:.3f}\n"
            f"CONTENT:\n{doc.page_content}"
        )
        cite = {
            "source": meta.get("source", "Unknown"),
            "url": meta.get("source_url", ""),
            "score": round(float(score), 3),
            "page": meta.get("page"),
        }
        if cite not in citations:
            citations.append(cite)
    if not context_parts:
        return (
            "I could not find relevant policy material in the current NaviCare knowledge base. "
            "Please ask an Admin to upload current MOH, CPF Board or AIC guidance.",
            [],
        )
    profile_text = "No profile details supplied."
    if profile:
        profile_text = "\n".join(
            f"{key}: {value}" for key, value in profile.items()
            if value not in (None, "", "Not provided")
        )
    prompt = (
        f"USER PROFILE (self-reported; not verified):\n{profile_text}\n\n"
        f"QUESTION:\n{question}\n\nRETRIEVED POLICY EXCERPTS:\n"
        + "\n\n---\n\n".join(context_parts)
    )
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        temperature=0.1,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content or "No response generated.", citations


def summarise_document(text: str, filename: str):
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is missing.")
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        temperature=0.1,
        messages=[
            {
                "role": "system",
                "content": (
                    "Summarise the supplied Singapore long-term care policy document. "
                    "Preserve dates, cohort conditions, amounts and exceptions exactly. "
                    "Do not add facts. State that the source document should be checked "
                    "for the authoritative wording."
                ),
            },
            {"role": "user", "content": f"Document: {filename}\n\n{text[:18000]}"},
        ],
    )
    return response.choices[0].message.content or "No summary generated."
