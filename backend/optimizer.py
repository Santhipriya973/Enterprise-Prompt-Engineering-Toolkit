from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def optimize_prompt(prompt):

    optimization_prompt = f"""
You are a Senior Prompt Engineering Expert.

Improve the following prompt.

Original Prompt:
{prompt}

Requirements:

Role
- Must start with "You are..."
- Mention at least 10 years of experience.
- Mention expertise.
- Mention professional behaviour.

Context
- Explain the business scenario.
- Give complete background.

Task
- Return as an array.
- Break into step-by-step instructions.

Rules
- Return as an array.
- Include professional constraints.
- Include "Think step by step."

Output Format
- Explain how the final answer should be presented.

Return ONLY valid JSON.

The JSON format MUST be exactly:

{{
    "optimized_prompt": {{
        "role": "Must always start with 'You are...'. Mention at least 10 years of experience, expertise and professional behaviour.",
        "context": "Provide detailed business context.",
        "task": [
            "Step 1",
            "Step 2",
            "Step 3"
        ],
        "rules": [
            "Rule 1",
            "Rule 2",
            "Think step by step."
        ],
        "output_format": "Specify the expected response format."
    }},
    "improvements": [
        "Improvement 1",
        "Improvement 2",
        "Improvement 3",
        "Improvement 4",
        "Improvement 5"
    ]
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": optimization_prompt
            }
        ],
        temperature=0.4
    )

    result = response.choices[0].message.content

    # Remove markdown if the AI accidentally returns it
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)