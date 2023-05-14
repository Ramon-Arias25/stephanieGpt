import configparser
import speech_recognition as sr
from gtts import gTTS
import pygame
import os

class Assistant:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.assistant_name = self.config.get('Assistant', 'assistant_name')
        self.activation_phrase = f"hey {self.assistant_name}"
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print(f"Listening for activation phrase: '{self.activation_phrase}'")
            audio = self.recognizer.listen(source)
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            if text.lower() == self.activation_phrase.lower():
                self.respond("Yes, how can I assist you?")

    def respond(self, response_text):
        tts = gTTS(text=response_text, lang='en')
        filename = "response.mp3"
        tts.save(filename)
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        #os.remove(filename)

if __name__ == '__main__':
    assistant = Assistant()
    while True:  # Keeps listening until you stop the program
        assistant.listen()
