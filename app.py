import os
import re
import io
from datetime import date
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI CareerFlow", page_icon="🚀", layout="wide")

SKILL_BANK = [
    "python", "linux", "aws", "azure", "docker", "kubernetes", "terraform",
    "jenkins", "github actions", "git", "networking", "sql", "excel",
    "communication", "troubleshooting", "monitoring", "grafana", "prometheus",
    "ci/cd", "bash", "shell scripting", "testing", "manual testing", "selenium",
    "fastapi", "streamlit", "pandas", "machine learning", "prompt engineering",
    "automation", "api", "rest api", "customer support", "ticket management",
    "windows", "incident management", "documentation"
]

SAMPLE_JOBS = [
    {
        "company": "CloudNova",
        "title": "Junior DevOps Engineer",
        "location": "Bengaluru, India",
        "description": "Support Linux systems, AWS cloud infrastructure, Docker containers, CI/CD pipelines using Jenkins, Git workflows, Bash scripting, monitoring, and incident troubleshooting.",
        "url": "https://example.com/jobs/junior-devops",
        "status": "Saved"
    },
    {
        "company": "HelpDeskPro",
        "title": "IT Service Desk Associate",
        "location": "Bengaluru, India",
        "description": "Provide Windows troubleshooting, networking fundamentals, ticket management, customer communication, incident documentation, and technical support.",
        "url": "https://example.com/jobs/service-desk",
        "status": "Applied"
    },
    {
        "company": "DataBridge",
        "title": "Cloud Support Associate",
        "location": "Remote, India",
        "description": "Troubleshoot AWS services, Linux, networking, Python automation, REST APIs, customer support cases, and technical documentation.",
        "url": "https://example.com/jobs/cloud-support",
        "status": "Interview"
    },
    {
        "company": "QualityWorks",
        "title": "QA Testing Trainee",
        "location": "Hybrid, India",
        "description": "Execute manual testing, create test cases, log defects, validate APIs, use SQL basics, document findings, and communicate with developers.",
        "url": "https://example.com/jobs/qa-trainee",
        "status": "Saved"
    },
]

def normalize(text):
    return re.sub(r"[^a-z0-9+#./ -]", " ", str(text).lower())

def extract_skills(text):
    normalized = normalize(text)
    found = []
    for skill in SKILL_BANK:
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, normalized):
            found.append(skill)
    return sorted(set(found))

def score_match(resume, description):
    resume_skills = set(extract_skills(resume))
    job_skills = set(extract_skills(description))
    if not job_skills:
        return 0, [], [], resume_skills, job_skills
    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    score = round(100 * len(matched) / len(job_skills))
    return score, matched, missing, resume_skills, job_skills

def make_prompt(title, company, description, matched, missing):
    return f"""You are a careful career assistant. Do not invent qualifications or experience.
Target role: {title} at {company}
Job description:
{description}

Skills evidenced by the supplied resume text and matching the description: {', '.join(matched) or 'None detected'}
Skills mentioned in the job description but not detected in the resume text: {', '.join(missing) or 'None detected'}

Tasks:
1. Summarize the role's key requirements.
2. Suggest truthful resume bullet improvements using only evidenced experience.
3. List the top skill gaps and one practical learning action for each.
4. Draft a concise, tailored application note.
5. Label assumptions clearly and ask for clarification instead of fabricating facts.
Keep the output concise and actionable."""

st.title("🚀 AI CareerFlow")
st.caption("A practical AI-assisted job matching and application workflow")
st.markdown("**Goal:** turn job-search notes into a repeatable workflow: compare → prioritize → track → improve.")

with st.sidebar:
    st.header("Candidate profile")
    default_resume = "AWS, Docker, Kubernetes, Jenkins, Terraform, Linux, Git, GitHub, Python, Bash, networking, troubleshooting, CI/CD, technical documentation, testing, incident management"
    resume_text = st.text_area("Paste resume text or skills", value=default_resume, height=180,
                               help="Demo text is prefilled. Replace it with your own content.")
    candidate_name = st.text_input("Profile label (optional)", "My Profile")
    st.divider()
    st.caption("Privacy: this demo processes text in the app session. Avoid entering sensitive personal data.")

if "jobs" not in st.session_state:
    st.session_state.jobs = pd.DataFrame(SAMPLE_JOBS)
if "selected_job" not in st.session_state:
    st.session_state.selected_job = 0

jobs = st.session_state.jobs.copy()
if "status" not in jobs.columns:
    jobs["status"] = "Saved"

total = len(jobs)
applied = int(jobs["status"].isin(["Applied", "Interview", "Offer", "Rejected"]).sum())
interviews = int((jobs["status"] == "Interview").sum())
offers = int((jobs["status"] == "Offer").sum())

m1, m2, m3, m4 = st.columns(4)
m1.metric("Jobs tracked", total)
m2.metric("Applications started", applied)
m3.metric("Interviews", interviews)
m4.metric("Offers", offers)

tab_match, tab_tracker, tab_add, tab_prompt = st.tabs(
    ["🎯 Match & prioritize", "📋 Application tracker", "➕ Add a job", "🧠 AI prompt copilot"]
)

with tab_match:
    st.subheader("Match your profile to a job")
    if jobs.empty:
        st.info("Add a job in the Add a job tab to get started.")
    else:
        labels = [f"{row['title']} — {row['company']}" for _, row in jobs.iterrows()]
        selected_label = st.selectbox("Choose a role", labels, index=min(st.session_state.selected_job, len(labels)-1))
        idx = labels.index(selected_label)
        row = jobs.iloc[idx]
        score, matched, missing, resume_skills, job_skills = score_match(resume_text, row["description"])
        left, right = st.columns([1, 2])
        with left:
            st.metric("Skill overlap score", f"{score}%")
            if score >= 70:
                st.success("Strong keyword overlap")
            elif score >= 40:
                st.warning("Partial overlap — review gaps")
            else:
                st.error("Low overlap — inspect requirements")
            st.caption("This is a transparent keyword-overlap indicator, not a hiring probability.")
        with right:
            st.write(f"**{row['title']}** at **{row['company']}**")
            st.write(f"📍 {row['location']}")
            if row.get("url"):
                st.markdown(f"[Open job listing]({row['url']})")
            st.write("**Detected matching skills**")
            st.write(", ".join(matched) if matched else "No matching skills detected from the current text.")
            st.write("**Potential skill gaps**")
            st.write(", ".join(missing) if missing else "No gaps detected from the supported skill list.")
        with st.expander("Show detected profile and job skills"):
            st.write("Profile skills:", ", ".join(sorted(resume_skills)) or "None")
            st.write("Job skills:", ", ".join(sorted(job_skills)) or "None")
        st.info("Tip: job descriptions and resumes can use different wording. Verify the result manually before making decisions.")

with tab_tracker:
    st.subheader("Application pipeline")
    edited = st.data_editor(
        st.session_state.jobs,
        use_container_width=True,
        hide_index=True,
        num_rows="dynamic",
        column_config={
            "status": st.column_config.SelectboxColumn("Status", options=["Saved", "Applied", "Assessment", "Interview", "Offer", "Rejected"], required=True),
            "url": st.column_config.LinkColumn("Job link"),
            "description": st.column_config.TextColumn("Description", width="large"),
        },
        key="job_editor"
    )
    st.session_state.jobs = edited
    csv_data = edited.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Export tracker as CSV", csv_data, file_name="careerflow_job_tracker.csv", mime="text/csv")
    st.caption("Sample companies and URLs are illustrative placeholders. Replace them with verified real listings.")

with tab_add:
    st.subheader("Add a vacancy")
    with st.form("add_job_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        company = c1.text_input("Company", placeholder="Company name")
        title = c2.text_input("Job title", placeholder="Junior Cloud Engineer")
        location = c1.text_input("Location", placeholder="Bengaluru / Remote")
        url = c2.text_input("Job URL (optional)", placeholder="https://...")
        description = st.text_area("Job description / key requirements", height=180)
        status = st.selectbox("Initial status", ["Saved", "Applied", "Assessment", "Interview", "Offer", "Rejected"])
        submitted = st.form_submit_button("Add job", type="primary")
        if submitted:
            if not company.strip() or not title.strip() or not description.strip():
                st.error("Please provide company, title, and job description.")
            else:
                new_row = pd.DataFrame([{"company": company.strip(), "title": title.strip(),
                                         "location": location.strip() or "Not specified",
                                         "description": description.strip(), "url": url.strip(), "status": status}])
                st.session_state.jobs = pd.concat([st.session_state.jobs, new_row], ignore_index=True)
                st.success("Job added. Open Match & prioritize to assess it.")
                st.rerun()

with tab_prompt:
    st.subheader("Prompt copilot")
    st.write("Generate a structured prompt for an external AI assistant. The prompt explicitly tells the model not to invent experience.")
    if not jobs.empty:
        prompt_labels = [f"{row['title']} — {row['company']}" for _, row in jobs.iterrows()]
        chosen = st.selectbox("Role for prompt", prompt_labels, key="prompt_job")
        row = jobs.iloc[prompt_labels.index(chosen)]
        score, matched, missing, _, _ = score_match(resume_text, row["description"])
        prompt = make_prompt(row["title"], row["company"], row["description"], matched, missing)
        st.text_area("Generated prompt", value=prompt, height=320)
        st.download_button("⬇️ Download prompt as TXT", prompt, file_name="careerflow_ai_prompt.txt", mime="text/plain")
        api_key = os.getenv("OPENAI_API_KEY", "")
        if api_key:
            st.success("OPENAI_API_KEY is configured. This starter build keeps external model calls disabled by default; use the generated prompt with your approved AI tool.")
        else:
            st.caption("No API key required for the demo. The matching engine runs locally; use the generated prompt with ChatGPT or another AI assistant for deeper language-based feedback.")

st.divider()
st.caption("AI CareerFlow • Assessment prototype • Review all AI suggestions before using them in real applications.")
