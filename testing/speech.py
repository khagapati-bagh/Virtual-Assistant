#resource link https://pypi.org/project/pyttsx3/
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text. Woow it's great")
name = "Radhe"
engine.say("my name is " + name, "saymyname")
engine.say("What a wonderful day")
engine.runAndWait()