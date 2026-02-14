from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import google.generativeai as genai

# 🔑 Add your Gemini API Key here
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

app = FastAPI()

# Home Page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>CurricuForge - AI Curriculum Generator</title>
        </head>
        <body style="font-family: Arial; padding: 40px;">
            <h2>CurricuForge : Generative AI–Powered Curriculum Design</h2>
            <form action="/generate" method="post">
                <label>Enter Course Name:</label><br><br>
                <input type="text" name="course" required style="width:300px;"><br><br>
                
                <label>Enter Target Audience:</label><br><br>
                <input type="text" name="audience" required style="width:300px;"><br><br>
                
                <button type="submit">Generate Curriculum</button>
            </form>
        </body>
    </html>
    """

# Generate Curriculum
@app.post("/generate", response_class=HTMLResponse)
def generate(course: str = Form(...), audience: str = Form(...)):
    
    prompt = f"""
    Create a structured curriculum for the course: {course}.
    Target Audience: {audience}.
    
    Include:
    1. Course Overview
    2. Modules with Topics
    3. Learning Outcomes
    4. Industry Relevance
    """

    response = model.generate_content(prompt)

    return f"""
    <html>
        <body style="font-family: Arial; padding: 40px;">
            <h2>Generated Curriculum</h2>
            <pre>{response.text}</pre>
            <br><a href="/">Generate Another</a>
        </body>
    </html>
    """
