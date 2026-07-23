# 🚀 Enterprise Prompt Engineering Toolkit

An AI-powered Enterprise Prompt Engineering Toolkit that helps users build, optimize, evaluate, compare, and manage prompts for Large Language Models (LLMs).

🌐 **Live Demo:**  
https://enterprise-prompt-engineering-toolkit-wsjkuz4c7fxue6davpjhjn.streamlit.app/

⚙️ **Backend API:**  
https://enterprise-prompt-engineering-toolkit.onrender.com

📚 **API Documentation:**  
https://enterprise-prompt-engineering-toolkit.onrender.com/docs

---

# 📖 Project Overview

The Enterprise Prompt Engineering Toolkit is a web application designed to help prompt engineers, developers, researchers, and AI enthusiasts create high-quality prompts for Large Language Models.

The toolkit provides:

- Prompt Builder
- Prompt Library
- Prompt Evaluator
- Prompt Optimizer
- AI Model Comparison
- Prompt Version History
- Analytics Dashboard

It improves prompt quality and allows users to compare responses from multiple AI models.

---

# ✨ Features

## 📝 Prompt Builder

- Create structured prompts
- Define Role
- Add Context
- Define Task
- Add Rules
- Specify Output Format
- Generate AI-ready prompts

---

## 📚 Prompt Library

- View all saved prompts
- Search prompts
- Delete prompts
- Store prompts in SQLite Database

---

## ⭐ Prompt Evaluator

Evaluates prompts based on:

- Clarity
- Completeness
- Context
- Structure
- Best Practices

Provides AI-generated feedback.

---

## 🚀 Prompt Optimizer

Optimizes prompts using AI by:

- Improving wording
- Increasing clarity
- Making prompts production-ready
- Preserving user intent

---

## 🤖 AI Model Comparison

Compare responses between multiple models:

- llama-3.3-70b-versatile
- openai/gpt-oss-20b

Displays:

- Response Time
- Word Count
- AI Response

---

## 🕒 Prompt Version History

Maintains multiple versions of prompts.

Features:

- View previous versions
- Restore any version
- Track changes

---

## 📊 Analytics Dashboard

Displays:

- Total Prompts
- Prompt Versions
- Available Models
- Latest Prompt
- Average Versions

---

# 🛠 Technology Stack

## Frontend

- Streamlit

## Backend

- FastAPI

## Database

- SQLite

## AI Models

- Groq API
- Llama 3.3 70B Versatile
- GPT OSS 20B

## Libraries

- Python
- Requests
- SQLAlchemy
- Pydantic
- Uvicorn
- Dotenv

---

# 🏗 Project Architecture

```
                    Streamlit Frontend
                           │
                           ▼
                    FastAPI Backend
                           │
        ┌──────────────────┼─────────────────┐
        ▼                  ▼                 ▼
 Prompt Engine       SQLite Database     Groq API
        │                                   │
        ▼                                   ▼
 Prompt Storage                     AI Model Responses
```

---

# 📂 Project Structure

```
Enterprise-Prompt-Engineering-Toolkit/

│
├── backend/
│   ├── streamlit_app/
│   │      └── app.py
│   │
│   ├── analytics.py
│   ├── compare_models.py
│   ├── database.py
│   ├── evaluator.py
│   ├── main.py
│   ├── models.py
│   ├── optimizer.py
│   ├── prompt_engine.py
│   ├── schemas.py
│   ├── prompt_toolkit.db
│   └── .env
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙ Installation

Clone repository

```bash
git clone https://github.com/Santhipriya973/Enterprise-Prompt-Engineering-Toolkit.git
```

Move into project

```bash
cd Enterprise-Prompt-Engineering-Toolkit
```

Install requirements

```bash
pip install -r requirements.txt
```

---

# ▶ Run Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Docs

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run Frontend

```bash
streamlit run backend/streamlit_app/app.py
```

---

# 📊 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /build_prompt | Generate Prompt |
| GET | /prompts | Get Prompt Library |
| DELETE | /prompts/{id} | Delete Prompt |
| POST | /evaluate | Evaluate Prompt |
| POST | /optimize | Optimize Prompt |
| POST | /compare_models | Compare AI Models |
| GET | /prompts/{id}/versions | Version History |
| GET | /analytics | Dashboard Analytics |

---

# 🚀 Deployment

## Backend

Render

https://enterprise-prompt-engineering-toolkit.onrender.com

---

## Frontend

Streamlit Community Cloud

https://enterprise-prompt-engineering-toolkit-wsjkuz4c7fxue6davpjhjn.streamlit.app/

---

# 📸 Screenshots

Add screenshots of:

- Dashboard
- Prompt Builder
- Prompt Library
- Prompt Evaluator
- Prompt Optimizer
- Model Comparison
- Version History
- Analytics

---

# 👩‍💻 Developer

**Bhavana Bogadi**

B.Tech Student

GitHub:

https://github.com/Santhipriya973

---

# ⭐ Future Enhancements

- User Authentication
- Team Collaboration
- Prompt Sharing
- Export to PDF
- Export to DOCX
- More AI Models
- AI Chat Assistant
- Prompt Templates
- Prompt Categories

---

# 📄 License

This project is developed for educational and learning purposes.
