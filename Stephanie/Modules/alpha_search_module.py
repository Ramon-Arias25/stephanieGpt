from Stephanie.Modules.base_module import BaseModule
from Stephanie.local_libs.wolframalpha_speech.index import WolframalphaSpeech
from Stephanie.local_libs.wolframalpha_speech.exceptions_manager import *


class AlphaSearchModule(BaseModule):
    def __init__(self, *args):
        super(AlphaSearchModule, self).__init__(*args)
        self.app_id = self.get_configuration('wolframalpha_search_engine_key')
        if self.app_id:
            self.client = WolframalphaSpeech(self.app_id)
        else:
            return False

    def do_a_search(self):
        status = False
        phrase = ""
        raw_text_array = self.raw_text.split()
        end_index = len(raw_text_array)
        for i in range(0, end_index):
            if status:
                phrase += " " + raw_text_array[i]
            elif raw_text_array[i] == "búsqueda":
                status = True
        if status is False:
            return "¿Puedes expresarlo un poco mejor?"
        phrase = phrase.strip()
        try:
            text = self.client.search(phrase)
        except ConfidenceError:
            return "Lo siento, no pude encontrar lo que pediste, tal vez intente ser un poco más específico."
        except InternalError:
            return "Parece que algo anda mal con el motor de búsqueda wolframalpha, tal vez intente preguntar más tarde."
        except MissingTokenError:
            print("Falta el TOKEN de API para el motor de búsqueda wolframalpha, diríjase a los documentos para ver cómo completar correctamente las configuraciones para el motor de búsqueda.")
            return "Parece que no ha proporcionado el TOKEN API para el motor de búsqueda, agréguelo en el archivo de configuración."
        except InvalidTokenError:
            print("Falta el TOKEN de API para el motor de búsqueda wolframalpha o no es válido, diríjase a los documentos para ver cómo completar correctamente las configuraciones para el motor de búsqueda.")
            return "Parece que no proporcionó el TOKEN de API o no es correcto para el motor de búsqueda, agréguelo en el archivo de configuración."
        return text
