from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

def regenerate_deobfuscation(code: str, prompt_template: str) -> str:
    if "{code}" in prompt_template:
        prompt = prompt_template.format(code=code)
    else:
        prompt = prompt_template + "\n\nObfuscated:\n```java\n" + code + "\n```\n\nDeobfuscated:\n"

    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content.strip()
