from groq import Groq
from dotenv import load_dotenv
import os
import re
import time
load_dotenv()
myapi_key=os.getenv("GROQ_API_KEY")
if not myapi_key:
    raise ValueError("key is not find")

client=Groq(api_key=myapi_key)
model="openai/gpt-oss-120b"
def get_amount(phone):
    if phone=="IQOOZ7s":
        return 19000
    elif phone=="IQOOZ6":
        return 16000
    else :
        return 0

def calculate(expression):
    if expression:
       return eval(expression)
    else :
        return "calcutation error"

tools={
    "get_amount":get_amount,
    "calculate":calculate
}
system_prompt='''
you are a phone shopping asistant , user will give you the prompt and you have to evalute every thing

you have two tools:
 1. get_amount(phone)
 2. calculate(expression)
how the argument should be pass in tools as
Action:get_amount("IQOOZ7s") not get_amount(phone="IQOOZ7s")
Action:calculate("2+4") not calculate(expression="2+4")

Follow these rules:
1.Decide what you need to do next.
2.Use only one tool at a time.
3.After finding the Action just stop immediate.
4.Don't guess anything or add guessed data in answer by yourself.
5.Wait until you recieve an observation.
6.Then decide your next step.
7. When the task is complete, give the Final Answer.

OUTPUT FORMAT:
  thought: what are you thinking to do 
  Action : tool_name(argument)

  When finished:
  Final Answer: your answer 
'''
def call_agent(user_prompt):
  message1={
      "role":"system",
      "content":system_prompt
  }
  message2={
      "role":"user",
      "content":user_prompt
  }
  messages=[message1,message2]
  for step in range(5):
      print('\n................')
      print(f"step:{step+1}")
      print('................')

      response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
      )
      answer = response.choices[0].message.content
      print(answer)

      
      if "Final Answer:" in answer:
            break

      match = re.search(
            r"Action:\s*(\w+)\((.*?)\)",
            answer
        )

      if match:

            tool_name = match.group(1)
            tool_input = match.group(2)
            tool_input = tool_input.strip()
            tool_input = tool_input.strip('"')

            if tool_name in tools:
                tool = tools[tool_name]
                observation = tool(tool_input)

            else:

                observation = "Tool not found"


            print(
                "Observation:",
                observation
            )


            messages.append({
                "role": "assistant",
                "content": answer
            })


            messages.append({
                "role": "user",
                "content":
                    "Observation: "
                    + str(observation)
            })
            time.sleep(5)

      
      
user_prompt='''
I have 20000 rs and I want to buy IQOOZ7s .you have to tell me did am i  able to buy it and if yes then how much money I have left over after buying this.
'''
call_agent(user_prompt)