import pyttsx3

text = "Hello, this is a sample text to be converted to speech."
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 170)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

engine.say(text)
engine.runAndWait()