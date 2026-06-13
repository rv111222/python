from openai import OpenAI
api_key = ""
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
prompt = "five points about java stream api"
model = "openai/gpt-4o-mini"
response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    stream=True
)
for chunk in response:
    content = chunk.choices[0].delta.content
    if content is not None:
        print(content, end="", flush=True)

# print(response.choices[0].message.content)
