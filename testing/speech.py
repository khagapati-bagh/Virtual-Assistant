#resource link https://pypi.org/project/pyttsx3/
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text. Wow it's great")
engine.runAndWait()
engine.say("What a wonderful day")
engine.runAndWait()