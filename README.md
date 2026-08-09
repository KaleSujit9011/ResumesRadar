<div align="center">

#  ResumeRadar
*Intelligent Resume Analyzer*

*An AI-powered career intelligence platform that analyzes resumes, identifies skill gaps, generates personalized interview questions, and builds actionable career roadmaps.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/Groq-API-F55036?style=for-the-badge)](https://groq.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-PDF%20Processing-3776AB?style=for-the-badge)](https://pypi.org/project/PyPDF2/)

<br/>

[**Get Started**](#-local-development-setup) &nbsp; • &nbsp;
[**Features**](#-features) &nbsp; • &nbsp;
[**Architecture**](#-architecture) &nbsp; • &nbsp;
[**API Reference**](#-api-reference) &nbsp; • &nbsp;
[**Report Issue**](https://github.com/KaleSujit9011/ResumeRadar.AI)

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

**ResumeRadar** is an AI-powered career intelligence application designed to help job seekers understand how effectively their resume aligns with a target role or career path.

Instead of providing generic resume recommendations, ResumeRadar analyzes the candidate's submitted resume, extracts relevant information, identifies potential skill gaps, generates role-specific interview questions, and produces a structured career development roadmap.

The application combines a **Flask backend**, document-processing libraries, a relational database, and the **Groq API** to provide an end-to-end resume analysis workflow.

### Key Outputs

ResumeRadar produces four primary outputs:

-  **Resume Analysis** — Identifies strengths, experience signals, and areas requiring improvement.
-  **Skill Gap Analysis** — Highlights missing or underrepresented technical, functional, and soft skills.
-  **Interview Questions** — Generates personalized questions based on the candidate profile and identified gaps.
-  **Career Roadmap** — Creates a structured learning and career development plan based on the user's goals.

### Target Users

ResumeRadar is designed for:

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
|  **Skill Gap Detection** | Compares the candidate's profile against target expectations and identifies missing or underrepresented skills. |
|  **AI-Powered Analysis** | Uses the Groq API to generate intelligent, contextual career recommendations from resume information. |
|  **Interview Question Generation** | Generates personalized technical and career-related interview questions based on the candidate profile. |
|  **Career Roadmap** | Creates a structured learning and career development plan for improving job readiness. |
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
| Processing | Resume analysis, skill-gap analysis, interview generation, roadmap generation |

---

##  Project Structure

> Update this structure if your actual repository contains additional files or different folder names.

```text
resumeradar/
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
<!-- 
##  Live Environment

The deployment information can be added here once the application is publicly hosted.

| Component | Environment |
|---|---|
| Frontend / Web App | `[Add deployed URL]` |
| Backend | Flask application |
| Database | `[Add database provider]` |
| Documentation | `[Add documentation URL]` |
| API / Swagger | `[Add if available]` |

> ⚠️ If ResumeRadar is deployed as a single Flask application serving the frontend, a separate frontend URL is not required.

--- -->

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
git clone https://github.com/your-username/resumeradar.git
cd resumeradar
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
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/resumeradar
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

##  Example Workflow

```text
1. Create an account / Log in
          ↓
2. Submit Resume
          ↓
3. Extract Resume Content
          ↓
4. Analyze Candidate Profile
          ↓
5. Identify Skill Gaps
          ↓
6. Generate Interview Questions
          ↓
7. Generate Career Roadmap
          ↓
8. Review Recommendations
```

### Typical User Journey

1. Sign up or log in.
2. Upload or submit resume content.
3. ResumeRadar extracts the resume information.
4. The AI analysis identifies strengths and improvement areas.
5. The system highlights missing or underrepresented skills.
6. Personalized interview questions are generated.
7. A structured career roadmap is created.
8. The user uses the recommendations to prepare for the target career path.

---

##  API Reference

The current project information does not provide a complete list of public REST API endpoints.

If the application exposes API routes, document them in the following format:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Check application/API status |
| `POST` | `/...` | Analyze submitted resume |
| `POST` | `/...` | Generate skill-gap analysis |
| `POST` | `/...` | Generate interview questions |
| `POST` | `/...` | Generate career roadmap |

Replace the placeholder endpoints with the actual Flask routes from the project.

### Example Request

```json
{
  "target_role": "Python Backend Developer",
  "resume_text": "..."
}
```

### Example Response

```json
{
  "analysis": {
    "strengths": [
      "Python",
      "Flask",
      "SQL"
    ],
    "improvement_areas": [
      "Cloud deployment",
      "System design"
    ]
  },
  "skill_gaps": [
    "Docker",
    "AWS"
  ],
  "interview_questions": [
    "How would you design a scalable Flask API?"
  ]
}
```

>  The JSON above is an illustrative response structure. Replace it with the actual response schema implemented by the application.

---

##  AI Processing Pipeline

ResumeRadar uses the Groq API as the AI processing layer.

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
| Skill Gap Detection | Identify missing or underrepresented skills relative to the target career path. |
| Interview Generation | Create questions relevant to the candidate's profile and gaps. |
| Roadmap Generation | Convert identified gaps into a structured development plan. |

---

##  Resume Processing

ResumeRadar supports document-based resume analysis.

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

An example of the type of insights ResumeRadar can generate:

```text
Resume Analysis:
- Strong backend development experience with Python and Flask.
- Resume would benefit from clearer project impact metrics.

Skill Gaps:
- Cloud deployment
- System design fundamentals
- SQL performance optimization

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

ResumeRadar follows [Semantic Versioning](https://semver.org/):

| Version | Purpose |
|---|---|
| **MAJOR** | Incompatible API or architecture changes |
| **MINOR** | Backward-compatible feature additions |
| **PATCH** | Backward-compatible bug fixes |

---

##  Links

- **GitHub Repository:** `https://github.com/your-username/resumeradar`
- **Live Demo:** `[Coming soon]`
- **Documentation:** `[Coming soon]`
- **Issue Tracker:** `https://github.com/your-username/resumeradar/issues`

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

-  Resume scoring against specific job descriptions
-  ATS compatibility analysis
-  Job-description-to-resume matching
-  Resume improvement tracking over time
-  More structured skill taxonomy and role mapping
-  Improved parsing for complex resume layouts
-  Exportable career reports
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

**Built with ❤️ for U.**

</div>