from google import genai
gclient = genai.Client(api_key="")
prompt="explain importance of api and api keys in short"
model = "gemini-2.5-flash"
response = gclient.models.generate_content(
    model=model,
    contents=prompt,
)
print(response.model_dump_json(indent=2))

