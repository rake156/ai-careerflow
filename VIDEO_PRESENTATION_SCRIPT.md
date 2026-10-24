# AI CareerFlow — Video Presentation Script (2–3 minutes)

**Recording tip:** Keep the application open while speaking. Use dummy profile text and the sample dataset. Speak naturally rather than reading every word.

## 0:00–0:25 — Introduction
Hello, and thank you for reviewing my AI Growth and Automation assessment. My project is AI CareerFlow, a small AI-assisted job matching and application workflow. The problem I wanted to solve is that job seekers often review vacancies manually, struggle to compare requirements with their skills, and track applications across different places.

## 0:25–0:50 — Tools and approach
I built the prototype in Python using Streamlit for the interface and pandas for managing job records and exporting them to CSV. I used an AI assistant to help break the problem into smaller requirements, draft the implementation, and refine the prompt that produces job-specific career guidance. The matching calculation itself runs locally, so the demo does not require an API key.

## 0:50–1:35 — Demonstrate the project
Here is the candidate profile on the left. I can replace this sample text with a resume summary or skills. In Match and Prioritize, I select a role. The app shows a keyword-overlap score, matching skills, and skills mentioned in the job description that were not detected in the profile. This makes the comparison easier to inspect.

Next, in the Application Tracker, I can update the status of a role, for example from Saved to Applied or Interview, and export the list as a CSV. In Add a Job, I can enter a new company, role, job description, and link. Finally, Prompt Copilot generates a structured prompt for an AI assistant to suggest truthful resume improvements and learning actions.

## 1:35–2:10 — Prompt engineering and problem-solving
I refined the prompts in stages. First, I defined the user problem and minimum features. Then I asked for a working prototype with input validation and clear limitations. One important refinement was to prevent fabricated qualifications. The generated prompt tells the AI to use only evidence from the resume, separate detected skills from gaps, label assumptions, and ask questions rather than inventing experience.

A second challenge was making the match score understandable. I labeled it as keyword overlap, not a probability of getting hired, because a simple skills list cannot capture every context or synonym.

## 2:10–2:35 — Outcome and next steps
The outcome is a working prototype that combines job comparison, application tracking, CSV export, and AI prompt generation in one workflow. The sample vacancies are placeholders, so real job details should be entered and verified before practical use. Future improvements could include secure resume file parsing, an optional language-model API, reminders, and permitted job-board integrations.

Thank you for watching. This project demonstrates how I used AI as a development partner while checking the result against practical requirements.

## Recording checklist
- [ ] Show the running app, not only slides.
- [ ] Demonstrate at least one match, one status edit, and prompt generation.
- [ ] Keep the video at least 2 minutes.
- [ ] Avoid showing personal contact information or API keys.
- [ ] Confirm the shared video link works for viewers.
