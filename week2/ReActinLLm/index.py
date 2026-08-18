from groq import Groq
from dotenv import load_dotenv
import os
import re
load_dotenv()
myapi_key=os.getenv("GROQ_API_KEY")
if not myapi_key:
    raise ValueError("key is not find")

client=Groq(api_key=myapi_key)
model="llama-3.3-70b-versatile"