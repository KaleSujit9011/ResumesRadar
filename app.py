import os
from flask import Flask, render_template, request,redirect,session
from db import Base, engine,SessionLocal
import models, PyPDF2 , docx,json
from ai_analyser import analyse_resume

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY")
if not secret_key and os.getenv("FLASK_DEBUG", "0") != "1":
    raise RuntimeError("SECRET_KEY is missing. Set it in your deployment environment variables.")
app.secret_key = secret_key or "dev-only-change-this-secret"
app.config["MAX_CONTENT_LENGTH"] = int(os.getenv("MAX_CONTENT_LENGTH", 5 * 1024 * 1024))
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = os.getenv("FLASK_DEBUG", "0") != "1"

Base.metadata.create_all(bind=engine)

SECTION_SCORE_KEYS = ("skills", "experience", "education", "projects", "keywords", "formatting")

def normalise_score(value):
    try:
        score = int(float(value))
    except (TypeError, ValueError):
        score = 0
    return max(0, min(100, score))

def normalise_section_scores(section_scores):
    if not isinstance(section_scores, dict):
        section_scores = {}

    return {
        key: normalise_score(section_scores.get(key, 0))
        for key in SECTION_SCORE_KEYS
    }

def normalise_analysis_result(result):
    if not isinstance(result, dict):
        return {
            "target_role": "",
            "ats_score": 0,
            "job_match_score": 0,
            "section_scores": normalise_section_scores({}),
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
            "error": "Analysis result was not in the expected format."
        }

    normalised = {
        "target_role": result.get("target_role", ""),
        "ats_score": result.get("ats_score", 0),
        "job_match_score": result.get("job_match_score", 0),
        "section_scores": normalise_section_scores(result.get("section_scores", {})),
        "role_fit_summary": result.get("role_fit_summary", ""),
        "matched_keywords": result.get("matched_keywords", []),
        "missing_keywords": result.get("missing_keywords", []),
        "skills": result.get("skills", []),
        "missing_skills": result.get("missing_skills", []),
        "skill_updates": result.get("skill_updates", []),
        "resume_updates": result.get("resume_updates", []),
        "resume_improvement_suggestions": result.get("resume_improvement_suggestions", []),
        "project_suggestions": result.get("project_suggestions", []),
        "priority_actions": result.get("priority_actions", []),
        "roadmap": result.get("roadmap", []),
        "interview_questions": result.get("interview_questions", [])
    }

    if "error" in result:
        normalised["error"] = result["error"]

    normalised["ats_score"] = normalise_score(normalised["ats_score"])
    normalised["job_match_score"] = normalise_score(normalised["job_match_score"])

    for key in (
        "matched_keywords",
        "missing_keywords",
        "skills",
        "missing_skills",
        "skill_updates",
        "resume_updates",
        "resume_improvement_suggestions",
        "project_suggestions",
        "priority_actions",
        "roadmap",
        "interview_questions"
    ):
        if not isinstance(normalised[key], list):
            normalised[key] = []

    if not isinstance(normalised["role_fit_summary"], str):
        normalised["role_fit_summary"] = ""
    if not isinstance(normalised["target_role"], str):
        normalised["target_role"] = ""

    return normalised

# home
@app.route("/") 
def home():
    if "user" in session:
        return redirect("/dashboard")  
    return redirect("/login")

# signup
@app.route("/signup",methods=["GET","POST"])
def signup():
    db = SessionLocal()
    try:
        if request.method =="POST":
            email = request.form.get("email")
            password  = request.form.get("password")

            existing_user = db.query(models.User).filter_by(email=email).first()
            if existing_user:
                return "User already exists"

            user = models.User(email=email, password=password)
            db.add(user)
            db.commit()

            return redirect("/login")
        return render_template("signup.html")
    finally:
        db.close()

#login
@app.route("/login",methods=["GET","POST"])
def login():
    db = SessionLocal()
    try:
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            user = db.query(models.User).filter_by(email=email).first()

            if user and user.password == password:
                session["user"] = user.email
                return redirect("/dashboard")
            else:
                return "Invalid credentials"

        return render_template("login.html")
    finally:
        db.close()

@app.route("/forgotpassword", methods=["GET", "POST"])
@app.route("/forgot-password", methods=["GET", "POST"])
def forgotpassword():
    message = None
    if request.method == "POST":
        email = request.form.get("email")
        message = f"If an account exists for {email}, password reset instructions will be sent."
    return render_template("forgotpassword.html", message=message)

#dashboard 
@app.route("/dashboard",methods=["GET","POST"])
def  dashboard():
    if "user" not in session:
        return redirect("/login")
    result = None
    if request.method == "POST":
        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")
        job_description = request.form.get("job_description", "")

        file = request.files.get("file")

        #file handling
        if file and file.filename != "":
            if file.filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                    resume_text = text
                except Exception as e:
                    result = {"error":f"PDF error:{str(e)}"}
            elif file.filename.endswith(".docx"):
                try:
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text + "\n"
                    resume_text = text
                except Exception as e:
                    result = {"error":f"Docx error:{str(e)}"}
        if resume_text and user_goal:
            try:
                result = normalise_analysis_result(analyse_resume(resume_text,user_goal,job_description))
                result["target_role"] = user_goal

                #save to db
                db = SessionLocal()
                try:
                    user = db.query(models.User).filter_by(email=session["user"]).first()
                    report = models.Reports(
                        user_id = user.id,
                        resume_text = resume_text,
                        result = json.dumps(result)
                    )
                    db.add(report)
                    db.commit()
                finally:
                    db.close()

            except Exception as e:
                result = {"error":f"AI Error:{str(e)}"}

    return render_template(
        "dashboard.html",
        user=session["user"],
        result=result
    )

#history
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")
    
    db = SessionLocal()
    try:
        user = db.query(models.User).filter_by(email=session["user"]).first()
        if not user:
            session.pop("user", None)
            return redirect("/login")

        report = db.query(models.Reports).filter_by(user_id= user.id).all()

        #JSON str to dict
        parsed_reports = []
        for r in report:
            try:
                parsed_result = normalise_analysis_result(json.loads(r.result))
            except:
                parsed_result = normalise_analysis_result({})

            parsed_reports.append({
                "resume":r.resume_text,
                "result":parsed_result
            })
        return render_template("history.html",reports=parsed_reports)
    finally:
        db.close()

#logout
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 5000)),
        debug=os.getenv("FLASK_DEBUG", "0") == "1"
    )

