import pandas as pd

def obter_produtos_unicos(df: pd.DataFrame):
    """Retorna a lista de produtos únicos."""
    if "Product" not in df.columns:
        return []
    return sorted(df["Product"].dropna().unique().tolist())

def obter_regioes_unicas(df: pd.DataFrame):
    """Retorna a lista de regiões únicas."""
    if "Region" not in df.columns:
        return []
    return sorted(df["Region"].dropna().unique().tolist())

def filtrar_dados(df: pd.DataFrame, data_inicio=None, data_fim=None, produtos=None, regioes=None) -> pd.DataFrame:
    """Filtra os dados por data, produto e região."""
    if "OrderDate" not in df.columns:
        return pd.DataFrame()

    df_copia = df.copy()
    df_copia["OrderDate"] = pd.to_datetime(df_copia["OrderDate"])

    if data_inicio:
        df_copia = df_copia[df_copia["OrderDate"] >= pd.to_datetime(data_inicio)]
    if data_fim:
        df_copia = df_copia[df_copia["OrderDate"] <= pd.to_datetime(data_fim)]

    if produtos and "Product" in df_copia.columns:
        df_copia = df_copia[df_copia["Product"].isin(produtos)]
    if regioes and "Region" in df_copia.columns:
        df_copia = df_copia[df_copia["Region"].isin(regioes)]

    return df_copia

def calcular_kpis(df: pd.DataFrame):
    """Calcula os indicadores chave de desempenho (KPIs)."""
    if df.empty:
        return {"vendas_totais": 0, "ticket_medio": 0, "pedidos_totais": 0, "regioes_ativas": 0}

    vendas_totais = float(df["TotalDue"].sum())
    pedidos_totais = df["SalesOrderID"].nunique() if "SalesOrderID" in df.columns else len(df)
    ticket_medio = vendas_totais / pedidos_totais if pedidos_totais else 0
    regioes_ativas = df["Region"].nunique() if "Region" in df.columns else 0

    return {
        "vendas_totais": vendas_totais,
        "ticket_medio": ticket_medio,
        "pedidos_totais": pedidos_totais,
        "regioes_ativas": regioes_ativas,
    }

def obter_vendas_por_produto(df: pd.DataFrame, top_n=10) -> pd.DataFrame:
    """Retorna o ranking dos produtos mais vendidos."""
    if df.empty or "Product" not in df.columns:
        return pd.DataFrame(columns=["Product", "TotalDue"])
    return (
        df.groupby("Product")["TotalDue"].sum()
        .reset_index()
        .sort_values("TotalDue", ascending=False)
        .head(top_n)
    )

def obter_vendas_ao_longo_do_tempo(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna a evolução diária das vendas."""
    if df.empty or "OrderDate" not in df.columns:
        return pd.DataFrame(columns=["OrderDate", "TotalDue"])
    return (
        df.groupby(df["OrderDate"].dt.date)["TotalDue"].sum()
        .reset_index()
        .rename(columns={"OrderDate": "OrderDate"})
    )
