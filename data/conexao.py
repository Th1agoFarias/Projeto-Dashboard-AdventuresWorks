import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def ler_query(caminho_arquivo: str) -> str:
    """Lê o conteúdo de um arquivo SQL e o retorna como uma string."""
    with open(caminho_arquivo, 'r') as file:
        return file.read()

def carregar_vendas_data():
    """
    Conecta ao banco de dados, executa uma consulta de um arquivo .sql
    e retorna os resultados em um DataFrame do Pandas.
    """
    try:
        server = os.getenv('DB_SERVER')
        port = os.getenv('DB_PORT', '1433')
        database = os.getenv('DB_NAME')
        username = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')

        connection_string = (
            f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?"
            "driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"
        )
        
        engine = create_engine(connection_string)
        query = ler_query('data/query.sql')
        
     
        df = pd.read_sql(query, engine)

  
        if 'OrderDate' in df.columns:
            df['OrderDate'] = pd.to_datetime(df['OrderDate'])
        
        return df
        
    except FileNotFoundError:
        st.error("ERRO: Arquivo query.sql não encontrado.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao conectar ou buscar dados: {e}")
        return pd.DataFrame()