from config import *
import openai

openai.api_key = OPENAI_KEY
text = input("Enter the text you want to know chit-chat or not\n")
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Check if the text is small talk or not,it is small talk it is of 6 letters or less or an overwhelm or happiness or any combination of emotions so it comes under chit-chat for eg: Gotcha, but not a small talk if it is straight up a sentence asking something or just a statement. If it is small talk Return only 'it is chit-chat' as output else 'It is not a chit-chat' as output\n{text}",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print(f"The answer is: {response['choices'][0]['text']}")
print("")
