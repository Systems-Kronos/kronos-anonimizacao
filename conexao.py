from dotenv import load_dotenv
import os
import psycopg2 as pg
from psycopg2 import Error

def conn():
    try:
        conecta = pg.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
    
        db_name = conecta.get_dsn_parameters()['dbname']
        print(f"Conexão bem sucedida ao banco de dados: {db_name}")
        return conecta
    except Error as e:
        print(f"Erro ao conectar com o banco de dados: {e}")

def desconecta(conecta):
    if conecta:
        conecta.close()
        print("Conexão encerrada.")
conn()