# openai-cli
OpenAI API Command Line Interface

## Install Dependencies

Install python dependencies.

```
pip install -r requirements.txt
```

## Set Environment Variable

Using OpenAI API requires an API key which needs to be set in the OPENAI_API_KEY environment variable. 

```
export OPENAI_API_KEY=<YOUR_API_KEY>
```

## Usage

```
openai-cli.py [-h] [-i INPUT] [-o OUTPUT] [-s SESSION] [-t TEMPERATURE] [-x MAX_TOKENS] [-d DIVERSITY]
              [-f FREQUENCY_PENALTY] [-p PRESENCE_PENALTY]

Enter an instruction and watch the API respond with a completion that attempts to match the context 
or pattern you provided.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Uses INPUT as prompt. Otherwise interactive prompt is activated.
  -o OUTPUT, --output OUTPUT
                        Saves session to OUTPUT file.
  -s SESSION, --session SESSION
                        Load session from SESSION file.
  -t TEMPERATURE, --temperature TEMPERATURE
                        Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the
                        model will become deterministic and repetitive.
  -x MAX_TOKENS, --max_tokens MAX_TOKENS
                        The maximum number of tokens to generate. Requests can use up to 4,000 tokens per session. (One token is
                        roughly 4 characters for normal English text)
  -d DIVERSITY, --diversity DIVERSITY
                        Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options considered.
  -f FREQUENCY_PENALTY, --frequency_penalty FREQUENCY_PENALTY
                        How much to penalize new tokens based on their existing frequency in the text so far. Decreases the
                        model's likelihood to repeat the same line verbatim.
  -p PRESENCE_PENALTY, --presence_penalty PRESENCE_PENALTY
                        How much to penalize new tokens based on whether they appear in the text so far. Increases the model's
                        likelihood to talk about new topics.
```



## Example

Below is an example session using the openai-cli utility. In this session the AI is talking about recent progress in AI technology. The session gets ended with quit and a session file is written to the sesssions folder.

```
$ ./openai-cli.py
openai-cli 0.0.1
OpenAI API Command Line Interface
Type "help" for usage information or "quit" to exit the utility.

>>> Tell me about the recent progress in AI technology!

Some of the recent progress in AI technology includes the development of more sophisticated algorithms, 
the increase in computing power and storage, and the availability of more data. This has resulted in AI systems 
that are more accurate and efficient than ever before.


>>> 
One area that has seen significant progress is in the field of machine learning. This is a subfield of AI that 
deals with the development of algorithms that can learn from data. Machine learning algorithms have been used 
to develop systems that can recognize objects, identify faces, and translate languages.



Another area of AI that has seen recent progress is in natural language processing (NLP). This is the ability of 
computers to understand human language. NLP algorithms have been used to develop chatbots and virtual assistants 
such as Siri and Alexa.


>>> quit
Session name: ai
```
