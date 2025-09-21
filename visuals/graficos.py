import plotly.express as px

# Cor primária para dar consistência aos gráficos
COR_PRIMARIA = "#1f77b4"

def criar_grafico_de_barras(dados):
    
    fig = px.bar(
        dados, 
        x='Product', 
        y='TotalDue',
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
        labels={'OrderDate': 'Data', 'TotalDue': 'Total de Vendas'},
        template='plotly_dark'
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_traces(line_color=COR_PRIMARIA)
    return fig