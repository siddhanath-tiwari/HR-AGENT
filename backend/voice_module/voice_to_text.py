import speech_recognition as sr

class VoiceToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_voice(self):
        """Converts spoken HR queries into text."""
        with sr.Microphone() as source:
            print("Listening for HR query...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except:
                return "Sorry, could not understand the query."