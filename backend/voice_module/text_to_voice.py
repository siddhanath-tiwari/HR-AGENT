import pyttsx3

class TextToVoice:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        """Converts AI-generated responses into voice output."""
        self.engine.say(text)
        self.engine.runAndWait()