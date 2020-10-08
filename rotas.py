from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer
from alunos import Alunos
import pyodbc
import logging

LOG_FORMAT = "%(levelname)s : %(filename)s : %(asctime)s : %(message)s"
logging.basicConfig(filename=".logs/ApiLogs",
                    level = logging.INFO,
                    format= LOG_FORMAT,
                    filemode= "w")
logger = logging.getLogger()

username = "BD19170"
password = ""

conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=regulus.cotuca.unicamp.br;'
                    'DATABASE=BD19170;'
                    'UID='+username+
                    ';PWD='+password)

cursor = conn.cursor()

app = Flask(__name__)

@app.route("/alunos", methods=["GET"])
def get_all_alunos():

    logger.info("Entrou get_all_alunos()")

    cursor.execute('SELECT * FROM Aluno')
    list_alunos = []

    for row in cursor:
        dados_aluno = Alunos()
        dados_aluno.ra = row[0]
        dados_aluno.nome = row[1]
        dados_aluno.email = row[2]
        list_alunos.append(dados_aluno.__dict__)

    return jsonify(list_alunos)

@app.route("/alunos/<ra>", methods=["GET"])
def get_alunos(ra):
    logger.info("Entrou get_all_alunos()")

    cursor.execute('SELECT * FROM Aluno where RA =' + ra)
    row = cursor.fetchone()

    dados_aluno = Alunos()
    dados_aluno.ra = row[0]
    dados_aluno.nome = row[1]
    dados_aluno.email = row[2]

    return jsonify(dados_aluno.__dict__)

@app.route("/alunos", methods=["POST"])
def post_alunos():
    return None

@app.route("/alunos", methods=["PUT"])
def put_Alunos():
    return None

@app.route("/alunos/<ra>", methods=["DELETE"])
def remove_Alunos(ra):
    return None

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    logger.info("Server running - localhost:5000")
    print("Server running - localhost:5000")
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()