# AI CareerFlow — Prompt Documentation

This document records the prompts used to plan, implement, test, and improve the assessment project. Keep the actual prompts you use; if you change the implementation, update this record honestly.

## Prompt 1 — Initial project selection
**Prompt**
> I need to complete an AI Skills & Prompt Engineering assessment. Build one practical project in the technology domain focused on automation. It must demonstrate meaningful AI use, prompt engineering, problem-solving, and a working outcome. Propose a small project that can be built and demonstrated reliably by a beginner.

**Purpose**
Select a project with a clear user problem and a feasible scope.

**Decision**
AI CareerFlow: a job-matching and application-tracking workflow.

## Prompt 2 — Requirements decomposition
**Prompt**
> Turn the AI CareerFlow idea into an MVP. Include inputs, outputs, user workflow, error states, privacy considerations, measurable success criteria, and features that can be demonstrated in under three minutes. Do not claim a feature exists unless it is implemented.

**Purpose**
Convert an idea into testable features rather than a slide-only concept.

**Outcome**
Resume text input, job description matching, skill gap display, status tracker, job entry form, CSV export, and prompt generation.

## Prompt 3 — Implementation
**Prompt**
> Build a small Python Streamlit app named AI CareerFlow. Implement a transparent keyword-overlap score from a bounded skills vocabulary, matched and missing skill lists, editable application statuses, adding a job, CSV export, and a prompt generator that forbids invented qualifications. Include sample data clearly labeled as illustrative. Do not implement web scraping or automatic application submission. Include input validation and explain scoring limitations.

**Purpose**
Generate a testable working application while limiting risky or misleading automation.

**Outcome**
A single-file Streamlit prototype plus requirements and run instructions.

## Prompt 4 — Prompt refinement: truthful AI output
**Prompt**
> Improve the job-specific prompt so an AI assistant must use only evidence from the supplied resume, distinguish detected skills from missing skills, label assumptions, suggest practical learning actions, and ask questions instead of inventing work history or qualifications. Keep it concise and structured.

**Purpose**
Make the generated AI prompt safer and more useful.

**Refinement**
Added explicit “Do not invent qualifications or experience” language and separate tasks for role requirements, resume bullets, skill gaps, and application note.

## Prompt 5 — Testing and edge cases
**Prompt**
> Review this app for empty input, jobs with no detected skills, invalid/incomplete job submissions, an empty tracker, CSV export, editable statuses, and misleading score claims. Provide a checklist of manual tests and fix any failures. Ensure sample employers and links are clearly described as placeholders.

**Purpose**
Test behavior, not just visual appearance.

**Manual test checklist**
- [ ] App opens with the sample dataset.
- [ ] Empty or unrelated resume text does not crash the matcher.
- [ ] A selected job shows a score, matched skills, and gaps.
- [ ] A job cannot be added without company, title, and description.
- [ ] A new job appears in the tracker and matcher.
- [ ] Status can be changed to Interview or Offer.
- [ ] CSV export downloads a readable CSV.
- [ ] Generated prompt says not to invent qualifications.
- [ ] Sample company names and URLs are identified as illustrative.
- [ ] The app describes the score as keyword overlap, not hiring probability.

## Prompt 6 — Video presentation script
**Prompt**
> Write a natural 2–3 minute presentation for AI CareerFlow. Explain the problem, chosen tools, how prompts were designed and refined, a walkthrough of the implemented features, one challenge and its solution, limitations, and next steps. Do not claim that API calls, scraping, or automatic applications exist.

**Purpose**
Keep the explanation aligned with the actual prototype.

## Iteration log template
Record any further changes you make:

| Iteration | Observation | Prompt/change | Result |
|---|---|---|---|
| 1 | Needed a demonstrable scope | Split idea into MVP features | A small working prototype |
| 2 | AI output could fabricate qualifications | Added explicit truthfulness constraints | Prompt emphasizes evidence and assumptions |
| 3 | Match score could be misunderstood | Added a visible limitation note | Score is labeled keyword overlap only |
| 4 | Demo data could be mistaken for live vacancies | Labeled sample records as placeholders | Clearer assessment demo |

**Integrity note:** This is a prepared prompt record for the project workflow. If you use other prompts or make further revisions, append them before submission so the document reflects your real process.
