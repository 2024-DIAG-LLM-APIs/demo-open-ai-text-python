from openai import OpenAI

client = OpenAI()

system = "Tu eres un microbiologo."

messages = [{
    "role": "system",
    "content": system
}]

while True:
    user = input("Tu: ")
    messages.append({
        "role": "user",
        "content": user
    })
    data = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    messages.append({
        "role": "assistant",
        "content": data.choices[0].message.content
    })
    print(data.choices[0].message.content)
