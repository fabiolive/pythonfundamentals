from pymongo import MongoClient

client = MongoClient('127.0.0.1')
db = client['dexterops']

def inserir_dados():
    try:
        db.fila.insert({"_id":1, "empresa":"4linux",
                        "cursos": [{"nome":"python fundamentals",
                                    "carga horária":40},
                                    {"nome":"linux fundamental",
                                    "carga horária":40}]})
    except Exception as e:
        print('Erro{}'.format(e))

inserir_dados()