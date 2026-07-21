from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def evaluate_prompt(prompt):

    evaluation_prompt = f"""
You are a Senior Prompt Engineering Reviewer with over 15 years of experience in Enterprise Prompt Engineering.

Evaluate the following prompt very strictly.

PROMPT:
{prompt}

Evaluate the following sections.

1. Role
- Is the role clearly defined?
- Does it mention experience?
- Does it mention expertise?
- Does it describe professional behaviour?

2. Context
- Is sufficient business context provided?
- Is the scenario understandable?

3. Task
- Are the instructions clear?
- Are the steps properly defined?

4. Rules
- Are constraints present?
- Does it include professional guidance?
- Does it include "Think step by step"?

5. Output Format
- Is the expected output clearly specified?

6. Clarity

7. Specificity

Scoring Guide

10 = Excellent
8-9 = Very Good
6-7 = Good
4-5 = Needs Improvement
0-3 = Poor

IMPORTANT:
Never give high scores if important sections are missing.

Return ONLY valid JSON.

Do NOT write explanations outside JSON.

The JSON format MUST be exactly:

{{
    "overall_score": 0,

    "scores": {{
        "role": 0,
        "context": 0,
        "task": 0,
        "rules": 0,
        "output_format": 0,
        "clarity": 0,
        "specificity": 0
    }},

    "strengths": [
        "...",
        "...",
        "..."
    ],

    "weaknesses": [
        "...",
        "...",
        "..."
    ],

    "suggestions": [
        "...",
        "...",
        "..."
    ]
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": evaluation_prompt
            }
        ],
        temperature=0.2
    )

    result = response.choices[0].message.content

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)