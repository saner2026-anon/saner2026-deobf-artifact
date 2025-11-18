from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

def evaluate_similarity(original: str, regenerated: str) -> str:
    prompt = f"""
You are a software code auditor.

Compare the two Java code snippets below and assess their similarity based only on the criteria used in the paper’s evaluation:
- Structural preservation (class/method structure, control flow, API/signature consistency)
- Naming quality (identifier consistency and meaningfulness)
- Readability and formatting (layout, indentation, clarity)

Do NOT evaluate functionality or executable behavior.  
Ignore comments, whitespace differences, and non-semantic formatting.

Factors to consider:
1. Consistency of class and method structure
2. Consistency of control flow patterns
3. Consistency of method signatures and identifiers
4. Naming similarity (whether identifiers correspond meaningfully)
5. Readability/layout similarity at the structural level

Provide:
- A brief explanation (1-3 sentences)
- A similarity score from 0 to 100

Scoring guide (aligned with the paper):
- 90-100: Excellent structural similarity
- 75-89: Intermediate similarity (minor structural or naming differences)
- 60-74: Fair similarity (noticeable structural/naming differences)
- 40-59: Poor similarity (significant structural changes or inconsistent identifiers)
- 0-39: Unusable (structurally different or inconsistent with the original)


Original:
```java
{original}
```
GPT:
```java
{regenerated}
```
Evaluation:
"""
    resp = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content.strip()
