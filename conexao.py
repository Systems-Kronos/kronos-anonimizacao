import os
from dotenv import load_dotenv
import psycopg2 as pg
from psycopg2 import Error
load_dotenv()
def conn():   
    try:
        conecta = pg.connect(
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            database = os.getenv("DB_NAME")
        )
        print("Conexão bem sucedida.")
        return conecta
    except Error as e :
        print(f"Erro ao conectar com o banco de dados: {e}")

def desconecta(conecta):
    if conecta:
        conecta.close()
        print("Conexão encerrada.")