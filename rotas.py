from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer
import logging

LOG_FORMAT = "%(levelname)s : %(filename)s : %(asctime)s : %(message)s"
logging.basicConfig(filename=".logs/ApiLogs",
                    level = logging.INFO,
                    format= LOG_FORMAT,
                    filemode= "w")
logger = logging.getLogger()

app = Flask(__name__)

@app.route("/alunos", methods=["GET"])
def get_all_alunos():
    return None

@app.route("/alunos/<ra>", methods=["GET"])
def get_alunos(ra):
    return None

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