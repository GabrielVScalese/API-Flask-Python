from flask import Flask, jsonify, request
import pyodbc
import json

app = Flask(__name__)

username = "BD19171"
password = "COTUCA78911INFO"

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=regulus.cotuca.unicamp.br;'
                      'DATABASE=BD19171;'
                      'UID=' + username +
                      ';PWD=' + password)

cursor = conn.cursor()


@app.route("/")
def raiz():
    return jsonify({"message": "API funcionando!"})


@app.route("/api/getPlayers")
def get_players():
    cursor.execute("Select top 4 * from Kitchny.dbo.Players order by pontuacao desc")

    list_players = []
    for row in cursor:
        player = {"nome": row[1], "senha": row[2], "nickname": row[3], "pontuacao": row[4]}
        list_players.append(player)

    return jsonify(list_players)


@app.route("/api/getPlayer/<nome>")
def get_player(nome):
    cursor.execute("Select * from Kitchny.dbo.Players where nome = '" + nome + "'")

    row = cursor.fetchone()

    player = {"nome": row[1], "senha": row[2], "nickname": row[3], "pontuacao": row[4]}

    return jsonify(player)


@app.route("/api/insertPlayer", methods=["POST"])
def insert_player():
    player = request.get_json()
    player_dict = json.loads(player)

    cursor.execute("Select * from Kitchny.dbo.Players where nome = '" + player_dict['nome'] + "'")

    row = cursor.fetchone()

    if row[1] == player_dict['nome']:
        return jsonify({"message": 500})

    cursor.execute("Insert into Kitchny.dbo.Players values (?,?,?,?)", player_dict['nome'], player_dict['senha'],
                   player_dict['nickname'], player_dict['pontuacao'])
    conn.commit()

    return jsonify(player_dict)


@app.route("/api/autenticatePlayer", methods=["POST"])
def autenticate_player():
    player = request.get_json()
    player_dict = json.loads(player)

    nome = player_dict['nome']
    cursor.execute("Select * from Kitchny.dbo.Players where nome = '" + nome + "'")

    for row in cursor:
        if str(row[2]) == player_dict['senha']:
            return jsonify({"message": 200})
        else:
            return jsonify({"message": 500})

    return jsonify({"message": 500})


@app.route("/api/updatePlayer", methods=["PUT"])
def update_player():
    player = request.get_json()
    player_dict = json.loads(player)

    cursor.execute("Update Kitchny.dbo.Players set nickname = '" + player_dict['nickname'] + "' where nome = '" + player_dict['nome'] + "'")
    cursor.commit()

    return jsonify({"message": 200})


app.run()
