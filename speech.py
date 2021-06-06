#!/bin/env python3


'''
Speech Recognition Program
by Ben Calvert
06 June 2021
'''

# Imports

import os
import json
import pprint
import pyttsx3
import speech_recognition as sr





class SpeechHub:

    def get_commands(self):
        c = sr.Recognizer()
        with sr.Microphone() as source:
            print ("listening...")
            c.pause_threshold = 0.7
            c.energy_threshold = 16380
            audio = c.listen(source)
            try:
                print("recognizing...")
    
                Query = c.recognize_google(audio, "en-US")

                print(("Query was: {0}").format(Query))

            except Exception as e:
                print(e)
                print("Pardon, I did not understand that.")
                return "None"

        return Query

    def Speak(self, audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.say(audio)
        engine.runAndWait()

    def quitSelf(self):
        print('Turn off Computer?')
        self.Speak('Turn Off Computer?')
        take = self.get_commands()
        choice = take
        if "yes" in choice:
            print("Shutting down PC in 15 secionds...")
            self.Speak('Shutting Down the Computer in 15 seconds.')
            os.system('shutdown -h 15')
        elif "no" in choice:
            print('Shutdown canceled')
            self.Speak('Shudown canceled.')

if __name__ == "__main__":
    ListenR = SpeechHub()
    ListenR.quitSelf()