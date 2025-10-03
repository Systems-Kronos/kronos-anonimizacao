# Importar as funções necessárias
import pandas as pd
import conexao as c

def get_dataframe(nome_tabela):
    conecta = None  # Inicializar a variável conecta
    try:
        conecta = c.conn()
        query = f"SELECT * FROM {nome_tabela};"  # Consulta dinâmica com o nome da tabela
        df = pd.read_sql_query(query, conecta)
        print(f"DataFrame criado com sucesso para a tabela: {nome_tabela}")
        return df
    except Exception as e:
        print(f"Erro ao criar DataFrame para a tabela {nome_tabela}: {e}")
    finally:
        if conecta:  
            c.desconecta(conecta)
    
    
df_empresa = get_dataframe('empresa')
df_usuario = get_dataframe('usuario')
print(df_empresa)
print(df_usuario)


    