import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(prompt):

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=4000)

    return(response['choices'][0]['text'].strip())