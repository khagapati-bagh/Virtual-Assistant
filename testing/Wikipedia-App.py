#Resource link https://pypi.org/project/wikipedia/1.4.0/

import wikipedia

while True:
	print("If you want to exit please type exit")
	var = input("Questions : ")
	if var == "exit":
		print("Bye See You Soon")
		break
	#wikipedia.set_lang("hi") #for setting languages
	print(wikipedia.summary(var, sentences = 3))
	print()
