from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

def evaluate_deobfuscation(original: str, regenerated: str, reference: str) -> str:
    prompt = f"""
You are a senior Java software auditor.

Compare the GPT-generated deobfuscation (candidate) with the reference implementation.
Your evaluation must cover:
1. Functional correctness — Do both versions do the same thing?
2. Structure — Are classes, methods, logic flow preserved?
3. Naming — Are the identifiers descriptive and appropriate?
4. Readability — Is the code readable, idiomatic, and well-structured?

After your written evaluation, assign a final quality score from 0 to 100:
- 90~100 = Excellent (equal or better than reference)
- 75~89  = Intermediate (minor issues or differences)
- 60~74  = Fair (functional but with clear issues)
- 40~59  = Poor (loss of logic or very bad naming)
- 0~39   = Unusable (completely broken or misleading)


Reference:
```java
{reference}
```

Candidate:
```java
{regenerated}
```
Evaluation:
"""
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content.strip()
