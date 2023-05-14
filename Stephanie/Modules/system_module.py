import datetime as dt
from Stephanie.Modules.base_module import BaseModule


class SystemModule(BaseModule):
    def __init__(self, *args):
        super(SystemModule, self).__init__(*args)
        self.name = self.get_configuration(section="USER", key="name")
        self.gender = self.get_configuration(section="USER", key="gender")

    def default(self):
        return "No entendi el comando, por favor repotelo!."

    def meaning_of_life(self):
         return "Recordar que lo mas importante tiene que ser siempre lo mas importante."

    def time_right_now(self):
        t = dt.datetime.now()
        return self.time_teller(t)

    def date_today(self):
        t = dt.datetime.now()
        return self.date_teller(t)

    def wake_up(self):
        t = dt.datetime.now()
        if self.gender:
            gender = self.gender.lower()
            if gender == "female":
                return "%s Señora!" % self.phase_of_the_day(t)
            else:
                return "%s Señor!" % self.phase_of_the_day(t)
        elif self.name:
            return "%s, %s!" % (self.phase_of_the_day(t), self.name)
        else:
            return "%s!" % self.phase_of_the_day(t)

    def go_to_sleep(self):
        self.assistant.events.add("sleep").trigger("sleep")
        return "Dormir es para débiles!"

    def quit(self):
        self.assistant.events.add("quit").trigger("quit")
        return "No estoy lista porque no te esfuerzas lo suficiente"
        return "Pero quiero mejorar, ingrato!"
        return "Volveré más fuerte!"

    def tell_system_status(self):
        import psutil
        import platform
        import datetime
        import locale

        locale.setlocale(locale.LC_ALL, 'es-ES') 
        os, name, version, _, _, _ = platform.uname()
        version = version.split('-')[0]
        cores = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        running_since = boot_time.strftime("%A %d. %B %Y")
        response = "Actualmente estoy corriendo en %s versión %s.  " % (os, version)
        response += "El nombre del equipo es %s y tiene %s núcleos de procesador.  " % (name, cores)
        response += "El uso actual de disco actual es de %s porciento.  " % disk_percent
        response += "El uso actual de la CPU es de %s porciento.  " % cpu_percent
        response += "El uso actual de la memoria es de %s porciento. " % memory_percent
        response += "Está encendido desde %s." % running_since
        return response

    @staticmethod
    def time_teller(time):
        t = time.strftime("%I:%M:%p")

        d = {0: "cero",
            1: "uno",
            2: "dos",
            3: "tres",
            4: "cuatro",
            5: "cinco",
            6: "seis",
            7: "siete",
            8: "ocho",
            9: "nueve",
            10: "diez",
            11: "once",
            12: "doce",
            13: "trece",
            14: "catorce",
            15: "quince",
            16: "dieciséis",
            17: "diecisiete",
            18: "dieciocho",
            19: "diecinueve",
            20: "veinte",
            30: "treint",
            40: "cuarenta",
            50: "cincuenta",
            60: "sesenta"}
        time_array = t.split(":")
        hour, minute, phase = int(time_array[0]), int(time_array[1]), time_array[2]
        return "La hora es: %s %s %s" % (hour, minute, phase)

    @staticmethod
    def date_teller(date):
        return date.strftime("It's %A, %d %B %Y today!")
        #return date.strftime("El dia de hoy es: %A, %d %B %!")

    @staticmethod
    def phase_of_the_day(time):
        hour = time.hour
        if hour < 12:
            return 'Good Morning'
            #return 'Buenos Dias'
        elif 12 <= hour < 18:
            return 'Good Afternoon'
            #return 'Buenas Tardes'
        if hour > 6:
            return 'Good Evening'
            #return 'Buenas Noches'
