from groq import Groq
from dotenv import load_dotenv
import json
import os


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
# base_url="https://api.groq.com/openai/v1"
client = Groq(api_key=api_key)

def analyse_resume(resume_text, user_goal, job_description=""):
    if not api_key:
        return {
            "target_role": user_goal,
            "ats_score": 0,
            "job_match_score": 0,
            "section_scores": {},
            "role_fit_summary": "",
            "matched_keywords": [],
            "missing_keywords": [],
            "skills": [],
            "missing_skills": [],
            "skill_updates": [],
            "resume_updates": [],
            "resume_improvement_suggestions": [],
            "project_suggestions": [],
            "priority_actions": [],
            "roadmap": [],
            "interview_questions": [],
            "error": "GROQ_API_KEY is missing from the .env file."
        }

    prompt = f"""
    You are a senior software engineer and hiring manager.
    Evaluate the resume based on the user's goal and job description.
    
    user goal:"{user_goal}"
    job description:"{job_description or "Not provided"}"
    
    STRICT RULES:
    - Extract only relevant skills for this goal
    - REMOVE irrelevant tools [excel for backend,etc]
    - Identify real Gaps
    - If job description is provided, match the resume against that job
      description and identify matched and missing keywords
    - Generate section-wise ATS scores for skills, experience, education,
      projects, keywords, and formatting
    - Give resume improvement suggestions that are specific and actionable
    - Create a targeted role report for the next role
    - Suggest what the candidate must update in skills, resume content,
      projects, keywords, and learning path
    - Generate roadmap only for missing fields
    - Make output DIFFERENT based on goal

    Return only JSON:
    {{
        "target_role":"{user_goal}",
        "ats_score":0,
        "job_match_score":0,
        "section_scores":{{
            "skills":0,
            "experience":0,
            "education":0,
            "projects":0,
            "keywords":0,
            "formatting":0
        }},
        "role_fit_summary":"",
        "matched_keywords":[],
        "missing_keywords":[],
        "skills":[],
        "missing_skills":[],
        "skill_updates":[],
        "resume_updates":[],
        "resume_improvement_suggestions":[],
        "project_suggestions":[],
        "priority_actions":[],
        "roadmap":[],
        "interview_questions":[]
    }}
    ats_score must be an integer from 0 to 100 based on resume relevance,
    keyword match, skill coverage, clarity, and role alignment.
    job_match_score must be 0 when no job description is provided; otherwise it
    must be an integer from 0 to 100 based on resume-to-job-description match.
    section_scores values must be integers from 0 to 100.
    role_fit_summary must be 2 to 3 concise sentences.
    matched_keywords and missing_keywords must come from the job description
    when provided.
    skill_updates must list skills the candidate should learn or improve.
    resume_updates must list exact resume improvements, keywords, sections,
    and bullet point changes needed for the target role.
    resume_improvement_suggestions must include practical edits to strengthen
    summary, experience bullets, projects, keywords, and formatting.
    project_suggestions must list portfolio projects that prove readiness for
    the target role.
    priority_actions must list the top 3 to 5 next actions in order.
    Resume:
    {resume_text}
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            messages=[
                {"role":"system","content":"you're a strict hiring manager."},
                {"role":"user","content":prompt}
            ]
        )

        content = response.choices[0].message.content.strip()

        start = content.find("{")
        end = content.rfind("}")+1

        if start == -1 or end == 0:
            raise ValueError(f"AI response did not contain valid JSON: {content}")

        return json.loads(content[start:end])

    except Exception as e:
        return {
            "target_role": user_goal,
            "ats_score": 0,
            "job_match_score": 0,
            "section_scores": {},
            "role_fit_summary": "",
            "matched_keywords": [],
            "missing_keywords": [],
            "skills":[],
            "missing_skills":[],
            "skill_updates":[],
            "resume_updates":[],
            "resume_improvement_suggestions":[],
            "project_suggestions":[],
            "priority_actions":[],
            "roadmap":[],
            "interview_questions":[],
            "error":str(e)
        }
