import json
import requests

user = json.dumps({'nome': 'Gabri', 'senha': '1234', "nickname": "teste", "pontuacao": 2})

ret = requests.post("http://localhost:5000/api/insertPlayer", json=user)
'''ret = requests.get("http://localhost:5000/api/getPlayers")'''

'''ret = requests.post("http://localhost:5000/api/autenticatePlayer", json=user)'''

'''print(ret.json())'''

print(ret.json())
