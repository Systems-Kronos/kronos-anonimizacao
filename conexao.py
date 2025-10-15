from dotenv import load_dotenv
import os
import psycopg2 as pg
from psycopg2 import Error

load_dotenv()

def conn():
    try:
        # Conecta o banco de dados
        conecta = pg.connect(
            dbname=os.getenv("DB_NAME"),  
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        # Printa o nome do banco de dados conectado
        db_name = conecta.get_dsn_parameters()['dbname']
        print(f"Conexão bem sucedida ao banco de dados: {db_name}")
        return conecta
    except Error as e:
        print(f"Erro ao 00conectar com o banco de dados: {e}")
        return None  # Retorna None explicitamente em caso de erro

def desconecta(conecta):
    if conecta: # Se a conexão existir, desconecta.
        conecta.close()
        print("Conexão encerrada.")
