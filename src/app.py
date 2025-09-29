import streamlit as st
from dotenv import load_dotenv

from data.conexao import carregar_vendas_data

from transformacao.transformacao import (
    obter_produtos_unicos, obter_regioes_unicas, calcular_kpis,
    obter_vendas_por_produto, obter_vendas_ao_longo_do_tempo, obter_vendas_por_regiao,
    calcular_ticket_medio_por_regiao

)
from visuals.graficos import (
    criar_grafico_de_barras, criar_grafico_de_linhas, criar_grafico_de_barras_regiao,criar_grafico_de_barras_por_regiao
    )

# --- Configuração da Página e Estilo ---
def configurar_pagina():
    st.set_page_config(
        page_title="AdventureWorks Dashboard",
        page_icon='bar_chart',       
        layout="wide"
    )
    st.markdown("""
    <style>
        .main { background-color: #0E1117; }
        .kpi-card {
            background-color: #1C1C2E; padding: 20px; border-radius: 10px;
            text-align: center; border: 1px solid #2A2A4A;
        }
        .kpi-card h3 { margin: 0; font-size: 16px; color: #A0A0B0; }
        .kpi-card p { margin: 5px 0 0 0; font-size: 28px; font-weight: bold; color: #FFFFFF; }
        h2 { color: #FFFFFF; border-bottom: 2px solid #1f77b4; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(show_spinner="Carregando e processando dados...")
def carregar_dados():
    return carregar_vendas_data()

# --- Componentes da Interface ---
def exibir_kpis(df):
    kpis = calcular_kpis(df)
    vendas_totais = f"US$ {kpis['vendas_totais']:,.2f}"
    ticket_medio = f"US$ {kpis['ticket_medio']:,.2f}"
    pedidos_totais = f"{int(kpis['pedidos_totais']):,}"
    regioes_ativas = int(kpis['regioes_ativas'])
    
    colunas = st.columns(4)
    dados_kpi = [
        ("Vendas Totais", vendas_totais), ("Ticket Médio", ticket_medio),
        ("Pedidos Totais", pedidos_totais), ("Regiões Ativas", regioes_ativas)
    ]
    for col, (rotulo, valor) in zip(colunas, dados_kpi):
        with col:
            st.markdown(f'<div class="kpi-card"><h3>{rotulo}</h3><p>{valor}</p></div>', unsafe_allow_html=True)

def exibir_graficos(df):
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Análises Visuais")
    col1, col2 = st.columns(2)
    with col1:
        # Gráfico de produtos
        vendas_por_produto = obter_vendas_por_produto(df, top_n=10)
        fig_barras = criar_grafico_de_barras(vendas_por_produto)
        st.plotly_chart(fig_barras, use_container_width=True)

        # Gráfico de regiões
        vendas_por_regiao = obter_vendas_por_regiao(df)
        fig_regiao = criar_grafico_de_barras_regiao(vendas_por_regiao)
        st.plotly_chart(fig_regiao, use_container_width=True)
        
    with col2:
        # Gráfico de evolução de vendas
        vendas_ao_longo_tempo = obter_vendas_ao_longo_do_tempo(df)
        fig_linhas = criar_grafico_de_linhas(vendas_ao_longo_tempo)
        st.plotly_chart(fig_linhas, use_container_width=True)

        # Gráfico de ticket médio por região
        ticket_medio_por_regiao = calcular_ticket_medio_por_regiao(df)
        fig_ticket_medio = criar_grafico_de_barras_por_regiao(ticket_medio_por_regiao)
        st.plotly_chart(fig_ticket_medio, use_container_width=True)

def main(): 
    load_dotenv()
    configurar_pagina()
    st.title("Dashboard de Vendas da AdventureWorks")

    df = carregar_dados()
    if df.empty:
        st.error("Não foi possível carregar os dados.")
        st.stop()
        
    st.sidebar.header("Filtros")
    
    df['Ano'] = df['OrderDate'].dt.year
    df['Mês'] = df['OrderDate'].dt.month
    
    anos_disponiveis = sorted(df['Ano'].unique(), reverse=True)
    meses_disponiveis = sorted(df['Mês'].unique())
    
    ano_selecionado = st.sidebar.selectbox("Ano", anos_disponiveis)
    mes_selecionado = st.sidebar.selectbox("Mês", meses_disponiveis)
    
    df_filtrado_por_data = df[(df['Ano'] == ano_selecionado) & (df['Mês'] == mes_selecionado)]
    
    produtos_disponiveis = obter_produtos_unicos(df_filtrado_por_data)
    produtos_selecionados = st.sidebar.multiselect("Produtos", produtos_disponiveis, default=produtos_disponiveis)
    
    regioes_disponiveis = obter_regioes_unicas(df_filtrado_por_data)
    regioes_selecionadas = st.sidebar.multiselect("Regiões", regioes_disponiveis, default=regioes_disponiveis)

    df_filtrado = df_filtrado_por_data[
        df_filtrado_por_data['Product'].isin(produtos_selecionados) &
        df_filtrado_por_data['Region'].isin(regioes_selecionadas)
    ]

    if df_filtrado.empty:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")
    else:
        exibir_kpis(df_filtrado)
        exibir_graficos(df_filtrado)
        st.markdown("<br>", unsafe_allow_html=True)
        st.header("Dados Detalhados")
        st.dataframe(df_filtrado)

if __name__ == "__main__":
    main() 