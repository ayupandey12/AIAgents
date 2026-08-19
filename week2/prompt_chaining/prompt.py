import os
from groq import Groq
from pathlib import Path
from dotenv import load_dotenv
import time

load_dotenv()
myapi_key=os.getenv("GROQ_API_KEY")
if not myapi_key:
    raise ValueError("key is not find")

client=Groq(api_key=myapi_key)
model="openai/gpt-oss-120b"
jd='''
Education: Bachelor’s or Master’s degree in Computer Science, Information Technology, or a related technical discipline.Experience: 0 to 2 years of professional software engineering experience or relevant technical internship history.Programming Languages: Proficiency in at least one modern backend or frontend language (e.g., Java, Python, C++, Go, JavaScript, or TypeScript).Core Computer Science Fundamentals: Strong foundational understanding of Data Structures, Algorithms, Object-Oriented Programming (OOP), and basic system design principles.Database Management: Basic experience working with relational databases (SQL) or NoSQL environments.Version Control: Hands-on familiarity with Git and standard version-control workflows.Problem-Solving: Proven ability to debug code, isolate runtime issues, and write clean, maintainable, and well-tested scripts.
'''
resume='''
Candidate Name:Alex MercerTechnical Skills:JavaPythonData Structures & AlgorithmsObject-Oriented Programming (OOP)SQL (MySQL)Git & GitHubProjects:Distributed Task Orchestrator APIRelational Database Indexing SimulatorAutomated Inventory Analytics Engine
'''
def call_llm(system_pm,user_pm):
    message1={
        "role":"system",
        "content":system_pm
    }
    message2={
        "role":"user",
        "content":user_pm
    }
    response=client.chat.completions.create(messages=[message1,message2],model=model)
    return response.choices[0].message.content

def step1_resumeskillextract():
    systempm='''
    you are a senior hr assistent . you have to extact only the skills of the candidate from the give resume.
    OUTPUT CONSTAINS:
    you have to just return skills of the candidate with comma sepreated and nothing more than that .don't add additional data by yourself.
    '''
    userpm=f'''
    this is my resume {resume} . you have to extract the skills from this resume.
    '''
    return call_llm(system_pm=systempm,user_pm=userpm)

def step2_jdskillextract():
    systempm='''
        you are a senior hr assistent . you have to extact only the skills of the jd from the give jd.Extract the skills carefully by reading it .don't add additional data by yourself.add skills which is optional or any of them skills want in another part so it is easy to understand and match from them.
        OUTPUT FORMAT:
        you have to just return skills of the jd with comma sepreated and  skills which are mutiple means anyone of them are required not all is in comma .don't add additional data by yourself.
        Example:
        frontend language (e.g., Java, Python, C++, Go, JavaScript, or TypeScript) so you have to return them in (java,python,c++,Go,javascript or typescript)
        '''
    userpm=f'''
        this is my jd {jd} . you have to extract the skills from this jd. 
        '''
    return call_llm(system_pm=systempm,user_pm=userpm)

def step3_match(cskills,jskills):
     systempm='''
        you are a senior hr assistent . you have to match the skills of candidate and skills required in jd . DONLT  add additional data by yourself just match them base on their given skills.
        OUTPUT FROMAT:
        you have to return the score in between 1 to 100 and return matching and nomatching list of the skills . don't add anything by yourself.
        Example:
        ( Java, Python, C++, Go, JavaScript, TypeScript) so you have to return full score for this section if any of one skill is matching from candidate skills.
        '''
     userpm=f'''
        this is the candidate skills {cskills} and this is the jd required skills {jskills}. you have to match them and return the score.
        '''
     return call_llm(system_pm=systempm,user_pm=userpm)

cskills=step1_resumeskillextract()
print(cskills)
time.sleep(3)
jskills=step2_jdskillextract()
print(jskills)
time.sleep(3)
result=step3_match(cskills,jskills)
print(result)