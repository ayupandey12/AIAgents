from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel
import os
load_dotenv()
myapi_key=os.getenv("GROQ_API_KEY")
if not myapi_key:
    raise ValueError("key is not find")
client=Groq(api_key=myapi_key)
class ticket(BaseModel):
    name:str
    email:str
    issue:str
Schema=ticket.model_json_schema()
message_system={
    "role":"system",
    "content":f"extract personal information fromt the ticket  in json format on strictly base of this schema {Schema}"
}
response_format={
    "type":"json_object"
}
text="my name is ayush pandey, my vill is banauta . my rolls rolls royce what i ordered  has scraches . my email is abs@gmail.com.my girlfriend name is nothing"
prompt=f"this is a customer ticket please extract presonal information from this. {text}"
model="llama-3.3-70b-versatile"
message={
    "role":"user",
    "content":prompt
}
response=client.chat.completions.create(
    messages=[message_system,message],
    model=model,
    response_format=response_format
)
res=response.choices[0].message.content
print(res)
import json
data=json.loads(res)
ticket=ticket(**data)
print(ticket.email)
