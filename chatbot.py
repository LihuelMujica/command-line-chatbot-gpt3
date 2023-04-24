import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


print("Bienvenido al chatbot en consola de Python")
username = input("Chatbot: Hola, soy chat gpt-3, ¿Cuál es tu nombre?:")

print("Chatbot: Hola, " + username + "! ¿En qué puedo ayudarte hoy?")

messages = []
while True:
    try:
        user_input = input(username + ": ")
        messages.append({ "role": "user", "content": user_input })
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
        )
        print("Chatbot: " + res["choices"][0]["message"]["content"])
    except KeyboardInterrupt:
        print("")
        print("Chatbot: Adios!!")
        break