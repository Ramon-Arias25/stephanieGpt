from Stephanie.Modules.base_module import BaseModule
import wikipedia


class WikipediaModule(BaseModule):
    def __init__(self, *args):
        super(WikipediaModule, self).__init__(*args)

    def give_a_summary(self):
        status = False
        phrase = ""
        raw_text_array = self.raw_text.split()
        for i in range(0, len(raw_text_array)):
            if status and raw_text_array[i] != "de" and raw_text_array[i] != "información":
                phrase += " " + raw_text_array[i]
            elif raw_text_array[i] == "wikipedia" or raw_text_array[i] == "Wikipedia":
                status = True

        if status is False:
            return "¿jefe no entiendo, puede expresarlo mejor?"
        
        phrase = phrase.strip()
        wikipedia.set_lang("es") 
        print(wikipedia.summary(phrase, sentences=3))  
        return(wikipedia.summary(phrase, sentences=3))  
        return "jefe no te puedo dar informacion de wikipedia de" + phrase + ", esté modulo aun está en construcción"