#!/usr/bin/python3

import os
import openai
import argparse

openai.api_key = os.getenv("OPENAI_API_KEY")



print("openai-cli 0.0.1")
print("OpenAI API Command Line Interface")
print("Type \"help\" for usage information or \"quit\" to exit the utility.")

# Initialize parser
parser = argparse.ArgumentParser(description="\nEnter an instruction and watch the API respond with a completion that attempts to match the context or pattern you provided.\n\n")

# Adding optional argument
parser.add_argument("-i", "--input", help = "Uses INPUT as prompt. Otherwise interactive prompt is activated.", type=str, default="")
parser.add_argument("-o", "--output", help = "Saves session to OUTPUT file.", type=str, default="")
parser.add_argument("-s", "--session", help = "Load session from SESSION file.", type=str, default="")
parser.add_argument("-t", "--temperature", help = "Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.", type=float, default=0.5)
parser.add_argument("-x", "--max_tokens", help = "The maximum number of tokens to generate. Requests can use up to 4,000 tokens per session. (One token is roughly 4 characters for normal English text)", type=int, default=256)
parser.add_argument("-d", "--diversity", help = "Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options considered.", type=float, default=1)
parser.add_argument("-f", "--frequency_penalty", help = "How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.", type=float, default=0)
parser.add_argument("-p", "--presence_penalty", help = "How much to penalize new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics.", type=float, default=0)


# Read arguments from command line
args = parser.parse_args()

# Check arguments
assert openai.api_key != None, "No API key provided. Set the environment variable OPENAI_API_KEY=<API-KEY>)."
assert args.temperature >= 0 and args.temperature <= 1, "temperature range is 0...1 (int)"
assert args.max_tokens >= 32 and args.max_tokens <= 4000, "max_token range is 32...4000 (float)"
assert args.diversity >= 0 and args.diversity <= 1, "diversity range is 0...1 (float)"
assert args.frequency_penalty >= 0 and args.frequency_penalty <= 2, "frequency_penalty range is 0...2 (float)"
assert args.presence_penalty >= 0 and args.presence_penalty <= 2, "presence_penalty range is 0...2 (float)"

# Get prompt and session
prompt = args.input
f = open(args.session)
session = f.read()
f.close()

# Print loaded session
print(session)

while True:

    # Get prompt
    if prompt == "":
        prompt = input(">>> ")
    else:
        print(">>> " + prompt)

    # Check for prompt key words
    if prompt == "exit" or prompt == "quit":
        break
    if prompt == "help":
        parser.print_help()
        continue

    # Add prompt to current session
    session = session + prompt
    
    # Execute OpenAI API request
    completion = openai.Completion.create(
        model="text-davinci-002",
        prompt=session,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        top_p=args.diversity,
        frequency_penalty=args.frequency_penalty,
        presence_penalty=args.presence_penalty,
        echo=False
        )["choices"][-1]["text"]
    
    # Print completion
    print(completion[1:] + "\n\n")
    
    # Add completion to current session
    session = session + completion + "\n\n\n" 

    # Clear prompt for next iteration
    prompt = ""
    

# Save session
if session != "":
    if args.output != "":
        name = args.output
    else:
        name = "sessions/" + input("Session name: ") + ".txt"

    if name != "":
        f = open(name, 'w')
        f.write(session)
        f.close()



