from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
my_apikey=os.getenv("GROQ_API_KEY")
if not my_apikey:
   raise ValueError("key is not find")

client=Groq(api_key=my_apikey)
model="llama-3.3-70b-versatile"

prompt='''
   patient will give you their  issue 
   I have problem in breathing .
   classify this
'''
message={
    "role":"user",
    "content":prompt
}
response=client.chat.completions.create(
   model=model,
   messages=[message]
)
print(response.choices[0].message.content)