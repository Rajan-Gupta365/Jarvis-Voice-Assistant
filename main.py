import pyttsx3 # module to convert text to audio
import speech_recognition as sr # module to use different class like recognizer, microphone,etc
import webbrowser # to open google, youtube, gmail, etc
import os # to open apps like notepad,whatsapp,etc
import datetime # to check current time


# setup for google api key
import google.generativeai as genai  
genai.configure(api_key="AIzaSyAV7nXYMei8jijfIPPfh8E17cDkFLXpnB0")  # connecting genai with  Gemini key
gemini_model = genai.GenerativeModel("models/gemini-2.5-flash") #selecting model to use

# function to get answer from Google Gemini model
def ask_ai(prompt):
    try:
        #model = genai.GenerativeModel("gemini-1.5-flash")  # defining model of gemini
        response = gemini_model.generate_content(prompt) # generating answer by using above model
        return response.text # .text to ignore extra answer like image or others
    except Exception as e: # it happen , when you go offline
        return "Sorry, I couldn't get the answer right now."



engine = pyttsx3.init() # starting module 
voices = engine.getProperty('voices') # fetching different types of language
engine.setProperty('voice', voices[1].id)  # female voice (like Alexa)
engine.setProperty('rate', 180)            
engine.setProperty('volume', 1.0)   # full volume






def speak(text):  # function to speak
    print(f"jarvis:{text}")
    engine = pyttsx3.init('sapi5') #here sapai5 is Speech api for microsoft to speak
    engine.say(text) # speak given text
    engine.runAndWait() # wait until text speaking work get finished


def take_command():
    r = sr.Recognizer() # its a class to make template of sound that recognize  speech from audio
    with sr.Microphone() as mic: # microphone is open automatically ones it call
        r.energy_threshold = 400 # to ignore other sounds(background noise) beyonds this limit
        r.pause_threshold = 0.6 # for staying to listen audio
        print("listening...")
        r.adjust_for_ambient_noise(mic, duration=0.5) # to avoid background noise
        try:
            audio = r.listen(mic,timeout = 3, phrase_time_limit=15) # your audi0 is recording here
        except Exception as e:
            print(f"Error: {e}")
            return ""
    try:
        query = r.recognize_google(audio,language='en-in') # fetching your audio from google api to identify your spoken words
        print(f"you said:{query}")
        return query.lower()
    except sr.UnknownValueError:
        print("i didnt understand it, plz repeat again")
        return ""
    except sr.RequestError:
        print("sorry, i am temporarily unavailable")
        return ""


def jarvis(): # main function definition
    speak("Initializing Jarvis") # speak funcion calling
    running = True # initializing first time as true 
    while running:
        commands = take_command()
        if "jarvis" in commands:
            speak("yes, i am listening") # to test whether jarivs is active or not
            while True:
                inputs = take_command()
                if(inputs==""):
                    continue
                elif "time" in inputs:
                    
                    curr_time = datetime.datetime.now().strftime("%I:%M %p")
                    #print(f"The current time is {curr_time}")
                    speak(f"The time is {curr_time}")
                    
                
                elif "google" in inputs:
                    #print("opening google")
                    speak("Google is opening")
                    webbrowser.open("http://google.com")

                elif "youtube" in inputs:
                # print("opening youtube")
                    speak("Youtube  is opening")
                    webbrowser.open("http://youtube.com")

                elif "gmail" in inputs:
                    #print("opening gmail")
                    speak("Gmail  is opening")
                    webbrowser.open("http://gmail.com")
                
                elif "whatsapp" in inputs:
                # print("opening whatsaap")
                    speak(f"your whatsapp is opening")
                    os.system("whatsapp")

                 
                elif "send message" in inputs:
                    speak("Please tell the phone number including country code")
                    number = take_command().replace(" ", "") # .replace to convert space into non-space 
                    speak("What should I say?")
                    message = take_command() # to take your msg to send
                    if number != "" and message != "":
                        import pywhatkit # importing here to use for individual work and to avoid heavy load
                        pywhatkit.sendwhatmsg_instantly(number, message)
                        speak("Message sent.")



                

                    

                elif "stop" in inputs or "quit" in inputs:
                    print("Thanks for your time")
                    running = False # condtion for outer looop
                    break # breaking inner loop





                
                # jarvis is integrating with AI 
                else:
                    try:
                        speak("Let me check that for you.")
                        response = ask_ai(inputs) #calling ask_ai function 
                        if response:
                            #print("AI Response:", response.text)
                            speak(response)
                        else:
                            speak("Sorry, I couldn't get the answer right now.")
                    except Exception as e: # it handles all error itself
                        #print("Error:", e)
                        speak(f"Sorry, something went wrong while connecting to AI. {e}")

        else:
            speak(f"unless you dont speak jarvis , you cannt enter perform your work:  {commands} ")

jarvis() # function calling to work 