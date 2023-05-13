import json
from openAIEngine.gpt_chat import chat_with_gpt
from modules.github_push import push_to_gpt

# Lee las extensiones de los lenguajes de programación desde un archivo JSON
with open('extensions.json') as json_file:
    EXTENSIONS = json.load(json_file)

def get_extension_from_response(response):
    """
    Esta función toma la respuesta de GPT como entrada y devuelve la extensión de archivo
    correspondiente basándose en el lenguaje de programación mencionado en la respuesta.
    """
    for language, extension in EXTENSIONS.items():
        if language in response.lower():
            return extension
    # Si no se encuentra ningún lenguaje de programación, devuelve '.txt' por defecto
    return ".txt"

# Solicita una conversación con GPT
response = chat_with_gpt("¿Cómo refactorizo este código Python para que sea más eficiente?")

# Obtén la extensión de archivo basándose en la respuesta de GPT
extension = get_extension_from_response(response)

# Escríbelo en un archivo con la extensión correcta
file_path = "response" + extension
with open(file_path, "w") as f:
    f.write(response)

# Ahora puedes hacer push de este archivo a GitHub
push_to_github("my-repo", file_path, "Refactorización basada en sugerencias de GPT")
