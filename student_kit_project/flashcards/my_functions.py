import pyttsx3

def say_word(text):
    """ function for text to speech"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()