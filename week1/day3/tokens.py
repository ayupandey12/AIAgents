import os
from groq import Groq
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
myapi_key=os.getenv("GROQ_API_KEY")
if not myapi_key:
    raise ValueError("key is not find")

client=Groq(api_key=myapi_key)
model="llama-3.3-70b-versatile"
prompt1="hello"
prompt2="give me the famous name of 10 cities"
prompt3="give me the essay on the good LLM model in 1000 words"
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
    "role":"user",
    "content":prompt
    }
    response=client.chat.completions.create(
      messages=[message],
      model=model,
      max_tokens=50 #limit your output token usage
    )
    print(response.choices[0].message.content)
    usage=response.usage
    print(f"finish reason is {response.choices[0].finish_reason}")
    print(f"prompttoken->{usage.prompt_tokens} , complisationtoken->{usage.completion_tokens}")