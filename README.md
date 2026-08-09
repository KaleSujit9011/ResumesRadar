<div align="center">

#  ResumesRadar
*Intelligent Resume Analyzer*

*An AI-powered career intelligence platform that analyzes resumes, matches them against target roles and job descriptions, scores ATS readiness, recommends resume improvements, generates personalized interview questions, and builds actionable career roadmaps.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/Groq-API-F55036?style=for-the-badge)](https://groq.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-PDF%20Processing-3776AB?style=for-the-badge)](https://pypi.org/project/PyPDF2/)

<br/>

[![Live Demo](https://img.shields.io/badge/Live-Demo-2ecc71?style=for-the-badge)](https://resumesradar.vercel.app/)

<br/>

[**Get Started**](#-local-development-setup) &nbsp; • &nbsp;
[**Features**](#-features) &nbsp; • &nbsp;
[**Architecture**](#-architecture) &nbsp; • &nbsp;
[**API Reference**](#-api-reference) &nbsp; • &nbsp;
[**Report Issue**](https://github.com/KaleSujit9011/ResumesRadar)

</div>

---

##  Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Live Environment](#-live-environment)
- [Local Development Setup](#-local-development-setup)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Environment Variables](#environment-variables)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [AI Processing Pipeline](#-ai-processing-pipeline)
- [Resume Processing](#-resume-processing)
- [Sample Output](#-sample-output)
- [Versioning](#-versioning)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## Overview

**ResumesRadar** is an AI-powered career intelligence application designed to help job seekers understand how effectively their resume aligns with a target role or career path.

Instead of providing generic resume recommendations, ResumesRadar analyzes the candidate's submitted resume, extracts relevant information, compares it with the next targeted role and optional job description, identifies potential skill gaps, generates role-specific interview questions, and produces a structured career development roadmap.

The application combines a **Flask backend**, document-processing libraries, a relational database, and the **Groq API** to provide an end-to-end resume analysis workflow.

### Key Outputs

ResumesRadar produces role-specific career outputs:

Current implemented outputs include:

- **Resume Analysis** - Identifies strengths, experience signals, and areas requiring improvement.
- **ATS Score** - Gives an overall resume readiness score for the selected target role.
- **Section-wise ATS Score** - Scores skills, experience, education, projects, keywords, and formatting separately.
- **Job Description Matching** - Compares the resume with a pasted job description and shows matched/missing keywords.
- **Skill Gap Analysis** - Highlights missing or underrepresented technical, functional, and soft skills.
- **Resume Improvement Suggestions** - Recommends practical edits for resume summary, bullets, projects, keywords, and formatting.
- **Interview Questions** - Generates personalized questions based on the candidate profile and identified gaps.
- **Career Roadmap** - Creates a structured learning and career development plan based on the user's goals.
- **Downloadable Analysis Report** - Lets users download the generated analysis as a text report.

### Target Users

ResumesRadar is designed for:

- Students preparing for placements
- Fresh graduates
- Early-career professionals
- Career switchers
- Job seekers preparing for interviews

---

##  Features

| Feature | Description |
|---|---|
|  **Resume Analysis** | Extracts and evaluates resume content to identify strengths, experience signals, and improvement areas. |
|  **Targeted Role Report** | Takes the candidate's next target role and generates a role-specific readiness report. |
|  **ATS Score** | Calculates an overall ATS-style score based on relevance, keyword coverage, skill fit, clarity, and role alignment. |
|  **Section-wise ATS Score** | Breaks scoring into skills, experience, education, projects, keywords, and formatting. |
|  **Job Description Matching** | Accepts an optional job description and identifies matched keywords, missing keywords, and job match score. |
|  **Skill Gap Detection** | Compares the candidate's profile against target expectations and identifies missing or underrepresented skills. |
|  **Resume Improvement Suggestions** | Provides actionable recommendations to improve resume summary, experience bullets, project descriptions, keywords, and formatting. |
|  **AI-Powered Analysis** | Uses the Groq API to generate intelligent, contextual career recommendations from resume information. |
|  **Interview Question Generation** | Generates personalized technical and career-related interview questions based on the candidate profile. |
|  **Career Roadmap** | Creates a structured learning and career development plan for improving job readiness. |
|  **Downloadable Report** | Allows users to download the generated resume analysis report from the dashboard or history page. |
|  **PDF Resume Processing** | Supports extracting text from PDF resumes using PyPDF2. |
|  **DOCX Resume Processing** | Supports processing resume documents using `python-docx`. |
|  **User Authentication** | Supports user sign-up/login functionality for accessing the application. |
|  **Persistent Storage** | Uses SQLAlchemy-compatible database storage for application data. |
|  **Web Application** | Provides a browser-based interface powered by the Flask application. |

---

##  Architecture

```text
                         ┌──────────────────────┐
                         │        User          │
                         │   Resume / Profile   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                     ┌───────────────────────────┐
                     │      Flask Web App        │
                     │     Application Layer     │
                     └─────────────┬─────────────┘
                                   │
                ┌──────────────────┼──────────────────┐
                │                  │                  │
                ▼                  ▼                  ▼
       ┌────────────────┐  ┌───────────────┐  ┌───────────────┐
       │ Resume         │  │ User /        │  │ AI Processing │
       │ Processing     │  │ Application   │  │ Layer         │
       │                │  │ Data          │  │               │
       │ PDF / DOCX     │  │ SQLAlchemy    │  │ Groq API      │
       └───────┬────────┘  └───────┬───────┘  └───────┬───────┘
               │                   │                  │
               └───────────────────┼──────────────────┘
                                   ▼
                         ┌──────────────────────┐
                         │   Analysis Results   │
                         ├──────────────────────┤
                         │ • Resume Analysis    │
                         │ • Skill Gaps         │
                         │ • Interview Questions│
                         │ • Career Roadmap     │
                         └──────────────────────┘
```

### Data Flow

```text
Resume Upload
     │
     ▼
File Type Detection
     │
     ├──────────────► PDF ──► PyPDF2
     │
     └──────────────► DOCX ─► python-docx
                              │
                              ▼
                       Extracted Resume Text
                              │
                              ▼
                        AI Processing
                              │
                         Groq API
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
        Resume Analysis   Skill Gaps     Interview Questions
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                       Career Roadmap
                              │
                              ▼
                         User Dashboard
```

---

##  Tech Stack

### Backend

| Layer | Technology |
|---|---|
| Programming Language | Python 3.10+ |
| Web Framework | Flask |
| ORM | SQLAlchemy |
| Database Driver | PyMySQL |
| AI API | Groq API |
| Environment Management | python-dotenv |
| Production Server | Gunicorn |

### Document Processing

| Component | Technology |
|---|---|
| PDF Extraction | PyPDF2 |
| DOCX Processing | python-docx |

### Database

| Component | Technology |
|---|---|
| ORM | SQLAlchemy |
| Compatible Database | MySQL / Other SQLAlchemy-supported databases |
| MySQL Driver | PyMySQL |

### AI Layer

| Component | Technology |
|---|---|
| AI Provider | Groq |
| Processing | Resume analysis, ATS scoring, job-description matching, skill-gap analysis, resume improvement suggestions, interview generation, roadmap generation |

---

##  Project Structure

> Update this structure if your actual repository contains additional files or different folder names.

```text
ResumesRadar/
├── app.py                    # Flask application entry point
├── requirements.txt          # Python dependencies
├── .env                      # Local environment variables
├── .env.example              # Environment variable template
├── Procfile                  # Production deployment configuration
│
├── templates/                # Flask HTML templates
│   ├── ...                   # Application pages
│   └── ...
│
├── static/                   # Static frontend assets
│   ├── css/
│   ├── js/
│   └── images/
│
├── models/                   # Database models
├── routes/                   # Application routes
├── services/                 # Business and AI processing logic
│
├── docs/
│   └── screenshots/          # Application screenshots
│
└── README.md                 # Project documentation
```

---

##  Local Development Setup

### Prerequisites

Make sure the following are installed:

- **Python 3.10+**
- **pip**
- **Git**
- **MySQL** or another SQLAlchemy-compatible database
- **Groq API key**

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ResumesRadar.git
cd ResumesRadar
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Core dependencies include:

```text
Flask
Groq
SQLAlchemy
PyMySQL
python-dotenv
PyPDF2
python-docx
gunicorn
```

---

##  Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=replace_with_a_long_random_secret
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/ResumesRadar
```

### Configuration

| Variable | Description |
|---|---|
| `SECRET_KEY` | Secret key used by Flask for application security/session management. |
| `GROQ_API_KEY` | API key used to access the Groq AI service. |
| `DATABASE_URL` | SQLAlchemy database connection string. |

---

##  Usage

Start the Flask application:

```bash
python app.py
```

The application should be available at:

```text
http://127.0.0.1:5000
```

### Production Server

For deployments using Gunicorn:

```bash
gunicorn app:app
```

---

### Typical User Journey

```text
1. Create an account / Log in
          ↓
2. Submit Resume
          ↓
3. Enter Target Role
          ↓
4. Paste Job Description (Optional)
          ↓
5. Extract Resume Content
          ↓
6. Generate ATS and Job Match Scores
          ↓
7. Identify Skill Gaps and Resume Improvements
          ↓
8. Generate Interview Questions and Career Roadmap
          |
          v
9. Review or Download Report
```
---

##  API Reference

ResumesRadar is currently a server-rendered Flask application. The routes below return HTML pages or redirects rather than public JSON API responses.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Redirects logged-in users to `/dashboard`; otherwise redirects to `/login`. |
| `GET` | `/signup` | Renders the sign-up page. |
| `POST` | `/signup` | Creates a new user account using submitted email and password. |
| `GET` | `/login` | Renders the login page. |
| `POST` | `/login` | Authenticates the user and starts a session. |
| `GET` | `/forgotpassword` | Renders the forgot-password page. |
| `POST` | `/forgotpassword` | Shows a password-reset instruction message. |
| `GET` | `/dashboard` | Renders the resume analysis dashboard for logged-in users. |
| `POST` | `/dashboard` | Accepts resume input/upload, target role, and optional job description; generates and stores the analysis report. |
| `GET` | `/history` | Shows saved analysis reports for the logged-in user. |
| `GET` | `/logout` | Clears the user session and redirects to `/login`. |

### Dashboard Analysis Form

`POST /dashboard` expects `multipart/form-data` because it supports file upload.

| Field | Type | Required | Description |
|---|---|---|---|
| `resume` | Text | Optional if `file` is provided | Plain pasted resume text. |
| `file` | File | Optional if `resume` is provided | Resume document upload. Supported formats: `.pdf`, `.docx`. |
| `role` | Text | Yes | Next targeted role, such as `Python Backend Developer` or `AI Engineer`. |
| `job_description` | Text | No | Optional job description used for job matching and keyword analysis. |

The dashboard route renders the generated report directly in `dashboard.html` and stores the report JSON in the `reports` table.

### Example Request

```http
POST /dashboard
Content-Type: multipart/form-data

resume=Experienced Python developer with Flask and SQL projects...
role=Python Backend Developer
job_description=We are hiring a backend developer with Python, Flask, REST APIs, Docker, SQL, and cloud deployment experience.
```

### Stored Analysis Result Schema

The AI result is normalized by the backend before it is displayed and saved.

```json
{
  "target_role": "Python Backend Developer",
  "ats_score": 78,
  "job_match_score": 72,
  "section_scores": {
    "skills": 80,
    "experience": 70,
    "education": 75,
    "projects": 82,
    "keywords": 68,
    "formatting": 85
  },
  "role_fit_summary": "The resume shows strong Python and Flask foundations but needs clearer backend impact metrics and deployment experience for the target role.",
  "matched_keywords": [
    "Python",
    "Flask",
    "SQL"
  ],
  "missing_keywords": [
    "Docker",
    "AWS",
    "REST API testing"
  ],
  "skills": [
    "Python",
    "Flask",
    "SQL"
  ],
  "missing_skills": [
    "Docker",
    "AWS"
  ],
  "resume_improvement_suggestions": [
    "Add measurable impact to project bullets.",
    "Include backend keywords from the job description.",
    "Mention API design, authentication, deployment, and database work clearly."
  ],
  "project_suggestions": [
    "Build and deploy a Flask REST API with authentication and MySQL.",
    "Create a resume parsing API with PDF/DOCX support and report history."
  ],
  "priority_actions": [
    "Add Docker and deployment experience.",
    "Rewrite project bullets with measurable outcomes.",
    "Add missing backend keywords from the job description."
  ],
  "interview_questions": [
    "How would you design a scalable Flask API?"
  ],
  "roadmap": [
    "Strengthen REST API design.",
    "Learn Docker basics.",
    "Deploy a Flask project with a cloud database."
  ]
}
```

---

##  AI Processing Pipeline

ResumesRadar uses the Groq API as the AI processing layer.

```text
Resume File
    │
    ▼
┌─────────────────────┐
│ Document Extraction │
│                     │
│ PDF → PyPDF2        │
│ DOCX → python-docx  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Resume Text         │
│ Normalization       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ AI Analysis         │
│      Groq API       │
└──────────┬──────────┘
           │
     ┌─────┼─────────────┬──────────────┐
     ▼     ▼             ▼              ▼
 Resume   Skill       Interview      Career
Analysis  Gaps        Questions      Roadmap
```

### AI Processing Tasks

| Task | Purpose |
|---|---|
| Resume Analysis | Understand the candidate's experience, skills, and strengths. |
| Targeted Role Analysis | Compare the candidate's resume with the next desired role. |
| ATS Scoring | Generate overall and section-wise resume readiness scores. |
| Job Description Matching | Compare resume content against a pasted job description and identify matched or missing keywords. |
| Skill Gap Detection | Identify missing or underrepresented skills relative to the target career path. |
| Resume Improvement Suggestions | Recommend practical edits to strengthen content, keywords, projects, and formatting. |
| Interview Generation | Create questions relevant to the candidate's profile and gaps. |
| Roadmap Generation | Convert identified gaps into a structured development plan. |

---

##  Resume Processing

ResumesRadar supports document-based resume analysis.

### Supported Formats

| Format | Processing Library |
|---|---|
| PDF | PyPDF2 |
| DOCX | python-docx |

### Processing Flow

```text
Uploaded Resume
      │
      ▼
File Type Detection
      │
      ├──── PDF ────► PyPDF2
      │
      └──── DOCX ───► python-docx
                         │
                         ▼
                  Extracted Text
                         │
                         ▼
                    AI Analysis
```

The extracted text is then passed to the application's analysis workflow for generating career intelligence.

---

##  Sample Output

An example of the type of insights ResumesRadar can generate:

```text
Target Role: Python Backend Developer

ATS Score: 78/100
Job Match Score: 72/100

Role Fit Summary:
The resume shows strong Python and Flask fundamentals but needs clearer backend project impact, API testing experience, and deployment proof for backend developer roles.

Section-wise ATS Score:
- Skills: 80/100
- Experience: 70/100
- Education: 75/100
- Projects: 82/100
- Keywords: 68/100
- Formatting: 85/100

Job Description Matching:
Matched Keywords:
- Python
- Flask
- SQL
- REST API

Missing Keywords:
- Docker
- AWS
- Unit testing

Skill Gaps:
- Cloud deployment
- System design fundamentals
- SQL performance optimization

Resume Improvement Suggestions:
- Add measurable results to project bullets, such as response time, users, records processed, or deployment outcome.
- Add missing backend keywords from the job description naturally in project and skills sections.
- Improve project descriptions by explaining problem, technology stack, implementation, and impact.

Interview Questions:
- How would you design a resume parsing pipeline for multiple file formats?
- How do you secure API keys in a Flask application?

Career Roadmap:
1. Strengthen database design and SQL skills.
2. Build and deploy a Flask project on a cloud platform.
3. Practice behavioral and technical interview questions weekly.
```

---

##  Screenshots

Recommended screenshots for the repository:

```text
docs/
└── screenshots/
    ├── dashboard.png
    ├── resume-analysis.png
    ├── skill-gaps.png
    ├── interview-questions.png
    └── career-roadmap.png
```

Add them to the README using:

```html
<p align="center">
  <img src="docs/screenshots/dashboard.png" width="800" />
</p>
```

---

##  Versioning

Current version:

**v1.0.0**

ResumesRadar follows [Semantic Versioning](https://semver.org/):

| Version | Purpose |
|---|---|
| **MAJOR** | Incompatible API or architecture changes |
| **MINOR** | Backward-compatible feature additions |
| **PATCH** | Backward-compatible bug fixes |

---

##  Links

- **GitHub Repository:** `https://github.com/KaleSujit9011/ResumesRadar`
- **Live Demo:** `https://resumesradar.vercel.app/`
- **Issue Tracker:** `https://github.com/KaleSujit9011/ResumesRadar/issues`

---

##  Contributing

Contributions are welcome.

### Development Workflow

1. Fork the repository.
2. Clone your fork.
3. Create a feature branch:

```bash
git checkout -b feature/your-feature-name
```

4. Implement your changes.
5. Test the application locally.
6. Commit your changes:

```bash
git add .
git commit -m "feat: add your feature"
```

7. Push the branch:

```bash
git push origin feature/your-feature-name
```

8. Open a Pull Request.

### Reporting Issues

When reporting an issue, include:

- Clear description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Relevant screenshots
- Error logs or traceback when applicable

---

##  Limitations & Future Improvements

### Current Limitations

- AI-generated recommendations depend on the quality and completeness of the submitted resume.
- Skill-gap analysis depends on the target role/context supplied to the application.
- AI outputs should be treated as career guidance rather than guaranteed hiring predictions.
- A complete API specification and automated evaluation metrics should be added as the backend evolves.

### Future Improvements

Potential improvements include:
-  Resume improvement tracking over time
-  More structured skill taxonomy and role mapping
-  Improved parsing for complex resume layouts
-  More granular authentication and authorization
-  Automated unit and integration testing
-  Production deployment with monitoring and logging

---

##  Author

**Sujit Kale**

AI & Data Science Undergraduate

**GitHub:** [https://github.com/KaleSujit9011](https://github.com/KaleSujit9011)

---

##  License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

<div align="center">

**Built with ❤️.**

</div>
