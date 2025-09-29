import plotly.express as px

COR_PRIMARIA = "#1f77b4"

def criar_grafico_de_barras(dados):
    
    fig = px.bar(
        dados, 
        x='Product', 
        y='TotalDue',
        title='Produtos Mais Vendidos',
        labels={'Product': 'Produto', 'TotalDue': 'Total de Vendas'},
        template='plotly_dark'
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis={'categoryorder':'total descending'},
        showlegend=False
    )
    fig.update_traces(marker_color=COR_PRIMARIA)
    return fig

def criar_grafico_de_linhas(dados):
    
    fig = px.line(
        dados, 
        x='OrderDate',  
        y='TotalDue',
        title='Vendas ao Longo do Tempo',
        labels={'OrderDate': 'Data', 'TotalDue': 'Total de Vendas'},
        template='plotly_dark'
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_traces(line_color=COR_PRIMARIA)
    return fig


def criar_grafico_de_barras_regiao(dados):
    """Cria um gráfico de barras horizontal para vendas por região."""
    fig = px.bar(
        dados,
        x='TotalDue',
        y='Region',
        orientation='h',
        title='Vendas por Região',
        labels={'Region': 'Região', 'TotalDue': 'Total de Vendas'},
        template='plotly_dark'
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis={'categoryorder':'total ascending'}
    )
    fig.update_traces(marker_color=COR_PRIMARIA)
    return fig 



def criar_grafico_de_barras_por_regiao(dados):
    """Cria um gráfico de barras horizontal para ticket médio por região."""
    fig = px.bar(
        dados,
        x='TicketMedio',
        y='Region',
        orientation='h',
        title='Ticket Médio por Região',
        labels={'Region': 'Região', 'TicketMedio': 'Ticket Médio'},
        template='plotly_dark'
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis={'categoryorder':'total ascending'}
    )
    fig.update_traces(marker_color=COR_PRIMARIA)
    return fig