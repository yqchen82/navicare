# NaviCare – AI-Powered Long-Term Care Scheme Navigator

A Streamlit RAG prototype for exploring Singapore's CareShield Life and ElderShield schemes using an Admin-managed policy knowledge base.

## What's included
- Refreshed UI inspired by the supplied NaviCare Francine reference: warm cream canvas, mint/teal accents, softer cards, updated typography, a branded sidebar and shared page styling.
- Basic Admin/User login.
- Admin document upload, indexing, listing and deletion.
- RAG-based policy Q&A with source names and URLs.
- Profile-assisted Scheme Navigator (birth year, residency, current cover and self-reported ADL context).
- About Us and Methodology pages.
- Bundled sample policy notes and the existing local policy library data.

The facelift changes presentation and shared UI components while retaining the existing NaviCare RAG modules and page workflows.

## Local setup
1. Install Python 3.11.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create your local environment file and configure your own credentials:
   ```bash
   cp .env.example .env
   ```
5. Add your OpenAI API key and non-default Admin/User passwords to `.env`.
6. Start the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Configuration
The app reads these settings from `.env` or Streamlit secrets:
- `OPENAI_API_KEY`
- `OPENAI_CHAT_MODEL` (default `gpt-4o-mini`)
- `OPENAI_EMBEDDING_MODEL` (default `text-embedding-3-small`)
- `ADMIN_USERNAME`, `ADMIN_PASSWORD`
- `USER_USERNAME`, `USER_PASSWORD`

Never commit `.env`, API keys, passwords or personal data. The supplied `.env.example` contains placeholders only. If a real API key has ever been included in a shared archive or repository, revoke it and create a replacement before continuing.

## Sample documents and local index
The `sample_docs/` directory contains attributed policy briefing notes for demonstration. The `data/` directory contains the project's local Chroma index and indexed policy documents. Review source URLs and dates and refresh the library with current official references before relying on it.

## Deployment (Streamlit Community Cloud)
1. Push this folder to a private or appropriately controlled GitHub repository without `.env`, personal data or secrets.
2. Create a Streamlit Community Cloud app and select `streamlit_app.py`.
3. Add the configuration values above in App Settings → Secrets.
4. Test both Admin and User roles after deployment.

**Persistence warning:** Streamlit Community Cloud local storage is ephemeral. Use managed persistent vector storage or rebuild the index from approved documents on startup for a stable deployment.

## Security and advice limitations
The environment-variable login is a classroom demonstration, not production authentication. Use an identity provider, password hashing, secure secret storage and appropriate access controls for real users. NaviCare is not a government service, insurer, medical assessor or financial adviser. It does not connect to Singpass/CPF accounts, calculate official personalised premiums, determine disability or approve claims. Verify policy details with CPF Board, MOH and AIC.
# chatbot-project
