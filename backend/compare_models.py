from groq import Groq
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODELS = [
    "llama-3.3-70b-versatile",
    "openai/gpt-oss-20b"
]

def compare_models(prompt):

    results = []

    for model in MODELS:

        try:

            start = time.time()

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3
            )

            end = time.time()

            answer = response.choices[0].message.content

            results.append({
                "model": model,
                "status": "success",
                "response_time": round(end - start, 2),
                "word_count": len(answer.split()),
                "response": answer
            })

        except Exception as e:

            results.append({
                "model": model,
                "status": "failed",
                "error": str(e)
            })

    return {
        "comparison": results
    }