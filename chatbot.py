import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


print("Bienvenido al chatbot en consola de Python")
username = input("¿Cuál es tu nombre?:")
