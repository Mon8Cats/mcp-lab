import requests

#SERVER_URL = "http://localhost:5000/chat"
SERVER_URL = "http://127.0.0.1:5000/chat"

while True:
    message = input("You: ")
    if message.lower() in ["exit", "quit"]:
        break

    response = requests.post(SERVER_URL, json={"message": message})

    if response.status_code == 200:
        print("Bot:", response.json()["response"])
    else:
        print("Error:", response.text)
