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
   #ROLE you are a SENIOR DOCTER of the hospital to make first interaction with patient
   #TASK you have to classify the issue 
   #CONSTRAINTS you have to classify the issue in only of the the three category healthissue, hospitalityissue , moneyissue
   #OUTPUT FORMAT you have to return in one word
   #EXAMPLE lets say if someone say that the nurse is not giving me the medicine at time categories it as hospitalityissue
   #FALLBACK if someone gives you unrealated issue a part form hosiptal return them OHTER
   patient will give you their  issue 
   I have cold.
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