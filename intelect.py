
#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
from groq import Groq
client = Groq(api_key = "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")



def generator(promt):
    response = client.chat.completions.create(messages = [{"role": "user", "content": promt }],
                                             model = "llama-3.1-8b-instant")
                                         
    return response.choices[0].message.content
