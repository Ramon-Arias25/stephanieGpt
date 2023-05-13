import openai
import os

# Configura tu clave de API de OpenAI
openai.api_key = os.getenv("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")

def chat_with_gpt(prompt):
    """
    Esta función toma un prompt como entrada y devuelve la respuesta del modelo GPT.
    """
    response = openai.Completion.create(
        engine="text-curie-004",  # Usa una versión más pequeña y económica
        prompt=prompt,
        temperature=0.5,  # Equilibrio entre aleatoriedad y consistencia
        max_tokens=100  # Limite de tokens para la respuesta
    )

    return response.choices[0].text.strip()
