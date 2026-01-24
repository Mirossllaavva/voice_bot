#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 
from groq import Groq
client = Groq(api_key = "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")
def generator(promt):
    response = client.chat.completions.create(messages = [{"role": "user", "content": promt }],
                                             model = "llama-3.1-8b-instant")
                                         
    return response.choices[0].message.content


