# AI CareerFlow — AI Growth & Automation Associate Task 1

A working prototype for technology-focused job-search workflow automation. It combines a local skill-overlap matcher, editable application tracker, CSV export, and a prompt copilot that creates a carefully constrained prompt for an external AI assistant.

## Features
- Compare resume text with job descriptions using a transparent skill-overlap score.
- Show detected matching skills and potential gaps.
- Track application status: Saved, Applied, Assessment, Interview, Offer, Rejected.
- Add custom jobs and export the tracker to CSV.
- Generate a reusable AI prompt for truthful, job-specific resume and application improvements.
- Runs locally without an API key; deeper language-model feedback can be performed by pasting the generated prompt into an approved AI assistant.

## Important limitations
- The match score is a keyword-overlap indicator, **not** a probability of being hired.
- Sample companies and job links are illustrative placeholders, not real vacancies.
- The built-in skill vocabulary is intentionally limited; resume wording can be missed.
- This starter build does not automatically scrape job boards or submit applications. It supports human-reviewed workflow automation and avoids unapproved mass applications.
- Do not upload sensitive personal data to public demos. Use dummy data for the recorded assessment.

## Run locally
Python 3.10 or newer is recommended.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Deploy free on Streamlit Community Cloud
1. Create a GitHub repository named `ai-careerflow`.
2. Upload `app.py`, `requirements.txt`, and this README.
3. Sign in to Streamlit Community Cloud using GitHub.
4. Choose **Create app**, select your repository and `app.py`, then deploy.
5. Test the public URL in a private/incognito window before submitting.
6. Use only dummy/demo resume text in the public deployment.

Deployment providers can change their free-tier limits. If Streamlit Community Cloud is unavailable for your account, run locally and submit a screen-recording plus the GitHub repository.

## Demo flow (2–3 minutes)
1. Introduce the problem: manual job review and scattered application tracking.
2. Show the profile text in the sidebar.
3. Select a sample role and explain the overlap score, matched skills and gaps.
4. Add a job with a custom description.
5. Change a status in the tracker and export CSV.
6. Open Prompt Copilot and explain how its prompt prevents fabricated experience.
7. Close with limitations and future improvements.

## Suggested future improvements
- Integrate a permitted LLM API with user consent and clear cost controls.
- Add file upload for PDF/DOCX resumes with local text extraction.
- Add reminders and calendar integration.
- Add validated job-board integrations only where permitted by the provider's terms.
- Store data in a database with authentication and access controls.
