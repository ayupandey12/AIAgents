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
message1={
    "role":"system",
    "content":"you are my oppenent team player"
}
message={
    "role":"user",
    "content":"i will defeat you"
}
response=client.chat.completions.create(
    messages=[message1,message],
    model=model
)
print(response.choices[0].message.content)