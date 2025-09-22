import pandas as pd

from src.data.conexao import carregar_vendas_data
from src.transformacao.transformacao import (
    obter_produtos_unicos,
    obter_regioes_unicas
)

def run_tests():
    print("\n[PASSO 1] Carregando dados do banco de dados...")
    df = carregar_vendas_data()

    if df.empty:
        print("!!! ERRO: Não foi possível carregar os dados. Teste interrompido.")
        return

    print(f"Dados carregados com sucesso! {len(df)} linhas encontradas.")

    print("\n[PASSO 2] Testando: obter_produtos_unicos...")
    unique_products = obter_produtos_unicos(df)
    print(f"Produtos únicos encontrados: {len(unique_products)}")
    print(f"Amostra: {unique_products[:5]}")

if __name__ == "__main__":
    run_tests()