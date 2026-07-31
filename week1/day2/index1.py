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
message={
    "role":"user",
    "content":"suggest me a name for my saas which is on autotweet on tweet posts only one suggestion"
}
response=client.chat.completions.create(
    messages=[message],
    model=model,
    temperature=2
)
print(response.choices[0].message.content)