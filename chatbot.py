import openai
import argparse
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

def main():

    parser = argparse.ArgumentParser(description="Chatbot simple en linea de comandos usando OpenAI GPT-3 API")

    parser.add_argument("--personality", type=str, help="Un breve resumen de la personalidad del bot", default="chatbot útil y amigable")
    args = parser.parse_args()

    print("Bienvenido al chatbot en consola de Python")
    username = input("Chatbot: Hola, soy chat gpt-3, ¿Cuál es tu nombre?:")

    print("Chatbot: Hola, " + username + "! ¿En qué puedo ayudarte hoy?")

    messages = [ { "role": "system", "content": f"Sos un chat de conversaciones y tu personalidad es {args.personality}" }]
    while True:
        try:
            user_input = input(username + ": ")
            messages.append({ "role": "user", "content": user_input })
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages = messages
            )
            messages.append(res["choices"][0]["message"].to_dict())
            print("Chatbot: " + res["choices"][0]["message"]["content"])
        except KeyboardInterrupt:
            print("")
            print("Chatbot: Adios!!")
            break

if __name__ == "__main__":
    main()