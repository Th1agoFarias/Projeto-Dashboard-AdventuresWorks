import os
import pandas as pd
from sqlalchemy import create_engine, text 
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def ler_query(caminho_arquivo: str) -> str:
    """Lê o conteúdo de um ficheiro SQL e retorna como string."""
    try:
        with open(caminho_arquivo, 'r') as file:
            return file.read()
    except FileNotFoundError:
        st.error(f"Ficheiro SQL não encontrado no caminho: {caminho_arquivo}")
        return ""

def carregar_vendas_data() -> pd.DataFrame:
    """
    Conecta ao banco de dados usando SQLAlchemy, executa uma consulta e retorna um DataFrame.
    """
    try:
        server = os.getenv('DB_SERVER')
        port = os.getenv('DB_PORT', '1433')
        database = os.getenv('DB_NAME')
        username = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')

        if not all([server, database, username, password]):
            st.error("Por favor, configure todas as variáveis de ambiente do banco de dados no seu ficheiro .env.")
            return pd.DataFrame()

        connection_string = (
            f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?"
            "driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"
        )

        engine = create_engine(connection_string)
        
        caminho_query = 'data/query.sql'
        query = ler_query(caminho_query)
        if not query:
            return pd.DataFrame()

        # CORREÇÃO: Envolve a query com a função text()
        df = pd.read_sql(text(query), engine)

        if 'OrderDate' in df.columns:
            df['OrderDate'] = pd.to_datetime(df['OrderDate'])

        return df

    except Exception as e:
        st.error(f"Ocorreu um erro ao conectar ou consultar o banco de dados: {e}")
        return pd.DataFrame()
