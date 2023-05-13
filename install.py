import importlib
import os
import subprocess

# El método inicializador de la clase Installer. Aquí, se inicializa la ruta del archivo de requisitos
# (por defecto, "requirements.txt") y se recuperan los módulos a instalar.
class Installer:
	def __init__(self, filename="requirements.txt"):
		self.filename = filename
		self.modules = self.get_modules()
	# Este método envuelve fetch_modules y clean_modules para obtener una lista limpia de módulos a instalar a partir del archivo de requisitos.
	def get_modules(self):
		raw_modules = self.fetch_modules(self.filename)
		return self.clean_modules(raw_modules)
	# Este método estático abre el archivo de requisitos y lee todas las líneas, cada una de las cuales debería representar un módulo.
	@staticmethod
	def fetch_modules(filename):
		with open("requirements.txt", "r") as f:
			modules = f.readlines()
			f.close()
		return modules
	# Este método estático limpia las líneas leídas del archivo de requisitos eliminando los caracteres de nueva línea ("\n")
	@staticmethod
	def clean_modules(modules):
		return [module.replace("\n", "") for module in modules]
	# Este es el método principal que verifica si cada módulo ya está instalado y, si no lo está, intenta instalarlo.
	# Imprime mensajes para informar al usuario sobre el estado de la instalación.
	def set_up(self):
		print("Setting up... Please wait...")
		for module in self.modules:
			status = self.check_if_installed(module)
			if status is not None:
				print("%s module is already successfully installed." % module)
			else:
				print("%s module is being installed..." % module)
				install_status = self.install_module(module)
				if install_status == 1:
					print("Some error caused in installing %s module. Kindly report back to the forum for further information on how to fix the problem." % module)
					break
				else:
					print("%s module was successfully installed." % module)
		print("\n")
		print("Everything is set up... And Stephanie is ready to run.")
		input("Close the command line by writting exit or simply close the window.")
	# Este método estático intenta encontrar el cargador para un módulo dado. Si el módulo ya está instalado,
	# importlib.find_loader(module_name) devolverá un objeto de cargador,
	# lo que significa que el módulo está instalado. Si el módulo no está instalado, se devolverá None.
	@staticmethod
	def check_if_installed(module_name):
		try:
			module_status = importlib.find_loader(module_name)
		except Exception:
			module_status = importlib.util.find_spec(module_name)
		return module_status
	# El método subprocess.run() ejecuta el comando proporcionado en una subshell.
	# En este caso, el comando es pip install {module_name}.
	# El argumento check=True hace que se lance una excepción subprocess.CalledProcessError si el comando devuelve un código de estado que indica un error
	# (por lo general, cualquier código de estado distinto de cero).
	@staticmethod
	def install_module(module_name):
        try:
            result = subprocess.run(['pip', 'install', module_name], check=True)
            return 0  # Devuelve 0 si el comando se ejecutó correctamente
        except subprocess.CalledProcessError:
            return 1  # Devuelve 1 si hubo un error en la ejecución del comando

if __name__ == '__main__':
	i = Installer()
	i.set_up()