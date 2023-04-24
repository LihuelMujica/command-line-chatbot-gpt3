import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


print("Bienvenido al chatbot en consola de Python")
username = input("Chatbot: Hola, soy chat gpt-3, ¿Cuál es tu nombre?:")

print("Chatbot: Hola, " + username + "! ¿En qué puedo ayudarte hoy?")

while True:
    try:
        user_input = input(username + ": ")
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [
                { "role": "user", "content": user_input }
            ]
        )
        print("Chatbot: " + res["choices"][0]["message"]["content"])
    except KeyboardInterrupt:
        print("Chatbot: Adios!!")
        break