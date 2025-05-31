
import os
import openai
import glob

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("Missing OPENAI_API_KEY environment variable.")

PROMPT_TEMPLATE = """
You are a senior software engineer. Analyze the following Python code for:
1. Readability
2. Maintainability
3. Naming conventions
4. Code smells or anti-patterns
5. Suggestions for refactoring or improvement

Respond in Markdown format.
Code:
```python
{code}
```
"""

def analyze_code(code: str) -> str:
    prompt = PROMPT_TEMPLATE.format(code=code)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content

def main():
    output_file = "AI_REVIEW.md"
    files = glob.glob("*.py")
    with open(output_file, "w") as out:
        for file in files:
            with open(file, "r") as f:
                code = f.read()
            out.write(f"## Analysis for `{file}`\n\n")
            try:
                analysis = analyze_code(code)
                out.write(analysis + "\n\n")
            except Exception as e:
                out.write(f"⚠️ Error analyzing {file}: {e}\n\n")

if __name__ == "__main__":
    main()
