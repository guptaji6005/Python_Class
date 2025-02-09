# import pyjokes

# joke = pyjokes.get_joke()
# print(joke)


import pyttsx3
engine = pyttsx3.init()
engine.say("Hey Ankur Gupta! What are you doing and when your go for sleep?")
engine.runAndWait()