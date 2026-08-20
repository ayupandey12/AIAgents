import os
from groq import Groq
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
myapi_key=os.getenv("GROQ_API_KEY")
if not myapi_key:
    raise ValueError("key is not find")

client=Groq(api_key=myapi_key)
model="openai/gpt-oss-120b"
message={
    "role":"user",
    "content":"Explain me how AI born and when ?"
}
# response=client.chat.completions.create(  #without streaming
#     messages=[message],
#     model=model
# )
# print(response.choices[0].message.content)
#streaming is best for userinterface 
streaming=client.chat.completions.create(model=model,messages=[message],stream=True)

for ch in streaming:
    content=ch.choices[0].delta.content
    if content:
        print(content,end="",flush=True)