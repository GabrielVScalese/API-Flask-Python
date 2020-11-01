from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/")
def raiz():
    return jsonify({"message": "API funcionando!"})


@app.route("/api/insertPlayer", methods=["POST"])
def insert_player():
    player = request.get_json()
    print(player)
    arquivo = open("Players.txt", "a+")
    arquivo.write("\n" + player)
    arquivo.close()
    return jsonify(player)


@app.route("/api/getPlayers")
def get_players():
    arquivo = open("Players.txt", "r+")
    linhas = arquivo.readlines()
    users = []
    for linha in linhas:
        if linha == "\n":
            continue
        else:
            user = json.loads(linha)
            users.append(user)
    return jsonify(users)


app.run()