from openai import OpenAI
client = OpenAI(api_key="")
prompt="five points about java stream api"
model = "gpt-5.5"
response = client.responses.create(
    model=model,
    input=prompt,
)
print(response.model_dump_json(indent=2))

