from openai import OpenAI

client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant, named Jarvis."},
        {
            "role": "user",
            "content": "What is the temperature today"
        }
    ]
)

print(completion.choices[0].message.content)

