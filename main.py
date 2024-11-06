import requests

response = requests.post('https://api.openai.com/v1/chat/completions', headers={
    "Authorization": "Bearer sk-proj-QzbQAqszchUA-Hzq3vOnB6JocFvJtJe3Gb8zluHqViIWg6PMDAaDvc5CY-PUMaDYjgnBCo4aFqBlbkFJW2Zg71pt74DVmiy9Ehal4Ns27zK1BvF-PO0KDJTCuMRbMiPAw_SdI5G9xCIzeQocLgZ7GL0PUA"
}, json={
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "Tu eres un microbiologo."
        },
        {
            "role": "user",
            "content": "Por que me enferme?"
        }
    ]
})

if response.status_code == 200:
    data = response.json()
    print(data['choices'][0]['message']['content'])
else:
    print("Error:", response.status_code)
