import requests
import urllib.parse
from Stephanie.configurer import config
from .exceptions_manager import *


class WolframalphaSpeech:
    def __init__(self, API_TOKEN=None):
        self.c = config
        self.API_TOKEN = self.c.config['MODULES']['wolframalpha_search_engine_key']
        
    def search(self, query):
        self.query_expression = urllib.parse.quote_plus(query)
        self.query_url = f"http://api.wolframalpha.com/v2/query?" \
             f"input={self.query_expression}" \
             f"&appid={self.API_TOKEN}" \
             f"&format=plaintext" \
             f"&output=json"
        return requests.get(self.query_url).json()["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
        
    def check_for_exceptions(self, request):
        status_code = request.status_code
        text = request.text
        if status_code == 501 or not text:
            raise ConfidenceError("La consulta no tiene la forma correctamente, esta mal escrita o es demasiado amplia.")
        if status_code == 400:
            raise InternalError("Algo está mal con el servidor, intente nuevamente más tarde.")
        if not request.ok:
            if text == "faltante Appid":
                raise MissingTokenError("Falta el TOKEN de API!")
            else:
                raise InvalidTokenError("Se proporcionó un TOKEN de API no válido.")
        return text
