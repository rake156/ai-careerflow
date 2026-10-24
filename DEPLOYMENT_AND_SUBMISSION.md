# Deployment and Submission Checklist

## A. Run and verify locally
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Create and activate a virtual environment.
4. Run `pip install -r requirements.txt`.
5. Run `streamlit run app.py`.
6. Test the flows in README and the prompt documentation.
7. Replace sample data only with information you have permission to use.

## B. Publish the source on GitHub
1. Create a public repository called `ai-careerflow` (or another clear name).
2. Upload `app.py`, `requirements.txt`, `README.md`, `PROMPT_DOCUMENTATION.md`, `VIDEO_PRESENTATION_SCRIPT.md`, and `DEPLOYMENT_AND_SUBMISSION.md`.
3. Add a short repository description: “AI-assisted job matching and application workflow prototype built with Python and Streamlit.”
4. Do not commit API keys, private resumes, passwords, or personal contact information.
5. Open the repository link in a signed-out/private browser to verify access.

## C. Optional live deployment
1. Sign in to Streamlit Community Cloud with GitHub.
2. Create a new app from your repository and select `app.py`.
3. Deploy and wait for the build to finish.
4. Test the public app on mobile and desktop.
5. Use dummy data in a public deployment. The current app uses session state and is not designed for secure long-term storage.

If free hosting is not available, submit the GitHub repository and a screen recording demonstrating the locally running app. Do not claim a live deployment until it has been tested.

## D. Record the presentation
1. Use the provided 2–3 minute script as a guide.
2. Record the running app with your voice explaining the workflow.
3. Demonstrate matching, adding/updating a job, CSV export, and prompt generation.
4. Upload the video to Google Drive or another accessible service.
5. Set sharing to allow the assessment team to view it, then test the link in a private window.

## E. Prepare the email
Recipient: jobs@gokulinfocare.com
Subject: AI Growth & Automation Associate — Task 1 Submission

Suggested email:
Hello Hiring Team,

Please find my Task 1 submission for the AI Growth & Automation Associate role.

Project: AI CareerFlow — Intelligent Job Matching & Application Automation

- Project repository / live demo: [insert verified link]
- Video presentation (2+ minutes): [insert verified link]
- Prompt documentation: [insert repository file or Drive link]

The project demonstrates a job-matching workflow, skill-gap visibility, application status tracking, CSV export, and structured prompt generation. I have included the project limitations and setup instructions in the README.

Thank you for your time and consideration.

Regards,
[Your name]

## Final checks
- [ ] Project link opens for anyone who needs to review it.
- [ ] Video is at least two minutes and has accessible permissions.
- [ ] Prompt documentation reflects the prompts and changes actually used.
- [ ] No secret keys or private personal data are published.
- [ ] Sample job entries are labeled as illustrative, not live vacancies.
- [ ] Run instructions work from a fresh environment.
