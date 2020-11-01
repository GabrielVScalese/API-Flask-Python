import json
import requests

user = json.dumps({'nome': 'Gabriel', 'pontuacao': 1000})

requests.post("http://localhost:5000/api/insertPlayer", json=user)
ret = requests.get("http://localhost:5000/api/getPlayers")

print(ret.json())
