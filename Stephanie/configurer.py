import os
import configparser
import json

# La clase Configurer tiene un constructor que acepta dos argumentos opcionales - filename y modules_filename.
# Estos representan los nombres de los archivos de configuración y de los módulos,
# respectivamente. Si no se proporcionan, se utilizan los valores predeterminados "config.ini" y "modules.json".
class Configurer:
    def __init__(self, filename="config.ini", modules_filename="modules.json"):
        print("initialised")
        self.abs_filename = self.get_abs_filename(filename)
        self.abs_mods_filename = self.get_abs_filename(modules_filename)
        self.config = configparser.ConfigParser()
        self.config.read(self.abs_filename)
        self.sections = self.config.sections()
        self.modules = self.retreive_modules(self.abs_mods_filename)
    # retreive_modules es un método estático que lee un archivo JSON y devuelve los datos en él. Si hay un error al leer el archivo o al analizar el JSON, se lanza una excepción.
    @staticmethod
    def retreive_modules(abs_mods_filename):
        print("modules retrieved.")
        try:
            with open(abs_mods_filename, "r") as file:
                modules = json.load(file)
                file.close()
        except Exception as e:
            raise Exception("Modules.json file has been not formatted correctly. check the support tab in case you're integrating some 3rd party module.") from e
        return modules
    #get_modules es un método que permite obtener los módulos de un archivo diferente al predeterminado.
    def get_modules(self, filename=None):
        if filename:
            abs_mods_filename = self.get_abs_filename(filename)
            return self.retreive_modules(abs_mods_filename)
        return self.modules
    # get_abs_filename es un método estático que devuelve la ruta absoluta de un archivo dado su nombre.
    @staticmethod
    def get_abs_filename(filename):
        return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.pardir, filename))
config = Configurer()