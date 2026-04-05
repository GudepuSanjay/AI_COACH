from groq import Groq
import os
from dotenv import load_dotenv
import json
import random

temperature = round(random.uniform(0.7, 1.0), 2)

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_question(subject, topic, micro_topic):

    prompt = f"""
You are an IBPS SO IT exam setter.

STRICT RULES:
- Output ONLY pure JSON
- NO explanation outside JSON
- NO markdown (no ```json)
- NO extra text
- Must be valid JSON

Format:
{{
 "question": "",
 "options": {{"A":"", "B":"", "C":"", "D":""}},
 "answer": "A",
 "explanation": ""
}}

Subject: {subject}
Topic: {topic}
Micro-topic: {micro_topic}
"""

    for _ in range(5):
        try:
            res = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                temperature=random.uniform(0.9, 1.3)
            )

            raw = res.choices[0].message.content.strip()

            # 🔥 CLEAN RESPONSE
            raw = raw.replace("```json", "").replace("```", "").strip()

            # 🔥 TRY DIRECT LOAD
            try:
                data = json.loads(raw)
            except:
                # 🔥 FALLBACK JSON EXTRACTION
                import re
                match = re.search(r'\{.*\}', raw, re.DOTALL)
                if match:
                    data = json.loads(match.group())
                else:
                    continue

            # ✅ VALIDATE
            if (
                isinstance(data, dict)
                and "question" in data
                and "options" in data
                and "answer" in data
                and "explanation" in data
            ):
                return data

        except Exception as e:
            print("Groq Error:", e)
            continue
   

    # 🚨 FINAL FALLBACK (ONLY ONCE)
    return {
        "question": f"In DBMS, which ACID property ensures complete execution?",
        "options": {
            "A": "Atomicity",
            "B": "Consistency",
            "C": "Isolation",
            "D": "Durability"
        },
        "answer": "A",
        "explanation": "Atomicity ensures all operations complete or none."
    }
