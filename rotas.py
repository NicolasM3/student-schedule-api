from flask import Flask, jsonify, request
from gevent.pywsgi import WSGIServer
from alunos import Aluno
from dbo import Alunos
import logging

LOG_FORMAT = "%(levelname)s : %(filename)s : %(asctime)s : %(message)s"
logging.basicConfig(filename=".logs/ApiLogs",
                    level = logging.INFO,
                    format= LOG_FORMAT,
                    filemode= "w")
logger = logging.getLogger()

app = Flask(__name__)

@app.route("/alunos/", methods=["GET"])
def get_all_alunos():

    logger.info("Entrou get_all_alunos()")

    list_alunos = Alunos.get_all()

    return jsonify(list_alunos)

@app.route("/alunos/<ra>", methods=["GET"])
def get_aluno(ra):
    #logger.info(f"Entrou get_aluno({ra})")

    dados_aluno = Alunos.get_aluno(ra)

    return jsonify(dados_aluno.as_dict())

@app.route("/alunos", methods=["POST"])
def post_alunos():
    data = request.json
    
    dados_aluno = Aluno()
    dados_aluno.ra = data["ra"]
    dados_aluno.nome = data["nome"]
    dados_aluno.email = data["email"]

    return jsonify(Alunos.insert_aluno(dados_aluno))

@app.route("/alunos", methods=["PUT"])
def put_Alunos():

    data = request.json
    
    dados_aluno = Aluno()
    dados_aluno.ra = data["ra"]
    dados_aluno.nome = data["nome"]
    dados_aluno.email = data["email"]

    return jsonify(Alunos.edit_aluno(dados_aluno))

@app.route("/alunos/<ra>", methods=["DELETE"])
def remove_Alunos(ra):
    return jsonify(Alunos.remove_aluno(ra))

if __name__ == '__main__':
    # Debug/Development
    # app.run(host="192.168.0.4", port="5000")
    # Production
    logger.info("Server running - localhost:5000")
    print("Server running - localhost:5000")
    http_server = WSGIServer(('192.168.0.4', 5000), app)
    http_server.serve_forever()