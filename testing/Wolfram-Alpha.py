#resource link https://pypi.org/project/wolframalpha/

import wolframalpha

var = input("Questions : ")
app_id = "PGQKHV-RHLPLGYULG"
client = wolframalpha.Client(app_id)

res = client.query(var)
answer = next(res.results).text

print(answer)