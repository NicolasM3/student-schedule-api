import pyodbc
from alunos import Aluno

username = "BD19170"
password = "BD19170"

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

        cursor.execute('SELECT * FROM Aluno where ra =?', ra)

        row = cursor.fetchone()

        dados_aluno = Aluno()

        if (row is None):
            return dados_aluno
        
        dados_aluno.ra = row[0]
        dados_aluno.nome = row[1]
        dados_aluno.email = row[2]

        return dados_aluno

    def insert_aluno(aluno):

        if(len(aluno.ra) > 5):
            return {"message" : "Error: Request Entity Too Large", "code": 413}

        cursor.execute('SELECT * FROM Aluno where ra =?', aluno.ra)

        row = cursor.fetchone()

        if (row is not None):
            return {"message" : "Error: Already in the DataBase", "code": 409}

        cursor.execute("insert into Aluno values(?, ?, ?)", aluno.ra, aluno.nome, aluno.email)
        conn.commit()

        return {"message" : "Post Sucessful", "code": 200}

    def edit_aluno(aluno):

        if(len(aluno.ra) > 5):
            return {"message" : "Error: Request Entity Too Large", "code": 413}

        cursor.execute('SELECT * FROM Aluno where ra = ? ', aluno.ra)

        row = cursor.fetchone()

        if (row is None):
            return {"message" : "Error: Not Found", "code": 404}

        if(aluno.nome == None):
            aluno.nome = row[1]

        if(aluno.email == None):
            aluno.email = row[2]

        print(aluno.as_dict())

        cursor.execute("update Aluno set nome = ?, email = ? where ra = ?", aluno.nome, aluno.email, aluno.ra)
        conn.commit()

        return {"message" : "Put Sucessful", "code": 200}
        
    def remove_aluno(ra):

        if(len(ra) > 5):
            return {"message" : "Error: Request Entity Too Large", "code": 413}

        cursor.execute("delete from Aluno where ra = ?", ra)
        conn.commit()

        return {"message" : "Remove Sucessful", "code": 200}