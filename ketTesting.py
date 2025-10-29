import pyttsx3

def speak(text):
    print(f"Jarvis: {text}")
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()

speak("Testing again.")
speak("Hi, my name is Rajan Gupta.")
