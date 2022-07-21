#!/usr/bin/python3

import os
import openai
import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = ""
session = ""
while True:

    prompt = input()
    
    if prompt[-4:] == "quit":
        break

    session = session + prompt
    
    completion = openai.Completion.create(
        model="text-davinci-002",
        prompt=session,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        echo=False
        )["choices"][-1]["text"]
    
    print(completion[1:] + "\n\n")
    
    session = session + completion + "\n\n\n" 


# Save session
timestamp = datetime.datetime.now().isoformat()
name = input("Session name: ")
f = open('sessions/' + timestamp + "_" + name + '.txt', 'w')
f.write(session)
f.close()



