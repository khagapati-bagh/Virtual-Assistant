import wikipedia
import wolframalpha

while True:
	print('If you want to exit please type exit')
	var = input("Question : ")

	if var == "exit":
		print("Bye See You Soon")
		break

	try:
		#wolframalpha
		app_id = "PGQKHV-RHLPLGYULG" #wolframalpha api id
		client = wolframalpha.Client(app_id) #creationg client
		res = client.query(var)#result
		answer = next(res.results).text #result in text format
		print(answer)
	except:
		#Wikipedia
		print(wikipedia.summary(var))
	print()