import pyodbc
from alunos import Aluno

username = "BD19170"
password = ""

conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=regulus.cotuca.unicamp.br;'
                    'DATABASE=BD19170;'
                    'UID='+username+
                    ';PWD='+password)

cursor = conn.cursor()

class Alunos:
    
    def get_all():
        cursor.execute('SELECT * FROM Aluno')
        list_alunos = []

        for row in cursor:
            dados_aluno = Aluno()
            dados_aluno.ra = row[0]
            dados_aluno.nome = row[1]
            dados_aluno.email = row[2]
            list_alunos.append(dados_aluno.as_dict())

        return list_alunos

    def get_aluno(ra):
        cursor.execute('SELECT * FROM Aluno where ra =' + ra)

        row = cursor.fetchone()

        dados_aluno = Aluno()
        dados_aluno.ra = row[0]
        dados_aluno.nome = row[1]
        dados_aluno.email = row[2]

        return dados_aluno