 PROJETO-DASHBOARD

## 📋 Descrição

O **PROJETO-DASHBOARD** é uma aplicação interativa para visualização e análise de dados, conectando-se a um banco de dados, executando consultas SQL e exibindo resultados em gráficos dinâmicos. O objetivo é facilitar o acompanhamento de KPIs e métricas relevantes para o negócio, de forma intuitiva e acessível.

---

## 📁 Estrutura do Projeto

```
PROJETO-DASHBOARD/
├── data/
│   └── query.sql              # Armazena a consulta SQL principal.
├── src/
│   ├── __init__.py
│   ├── app.py             # Interface principal do dashboard.
│   ├── data/
│   │   └── conexao.py     # Lógica de conexão com o banco.
│   ├── utils/
│   │   └── transformacao.py # Funções de processamento e KPIs.
│   └── visuals/
│       └── graficos.py    # Funções para criar os gráficos.
├── tests/
│   └── teste_processamento.py  # Script para testar as funções.
├── .env                        # Variáveis de ambiente.
├── .gitignore                  # Arquivos a serem ignorados.
├── requirements.txt            # Dependências do projeto.
├── run.py                      # Script para iniciar a aplicação.
└── README.md                   # Documentação do projeto.

```

---

## ⚙️ Configuração e Instalação

Siga os passos abaixo para executar o projeto localmente.

**1. Clone o Repositório:**
```bash
git clone [URL_DO_SEU_REPOSITORIO_AQUI]
cd PROJETO-DASHBOARD
```

**2. Crie e Ative um Ambiente Virtual:**
```bash
# Para Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
.\venv\Scripts\activate
```

**3. Instale as Dependências:**
```bash
pip install -r requirements.txt
```

**4. Configure as Variáveis de Ambiente:**
Crie um arquivo chamado `.env` na raiz do projeto e preencha com as suas credenciais de acesso ao banco de dados:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

**5. Edite a Consulta SQL:**
No arquivo `data/query.sql`, ajuste a consulta conforme sua necessidade.

---

## 🚀 Como Executar

Com o ambiente virtual ativado e o arquivo `.env` configurado, execute o dashboard:

```bash
python run.py
```
Ou, se estiver usando Streamlit:
```bash
streamlit run.py
```

O dashboard será aberto automaticamente no seu navegador (geralmente em `http://localhost:8501`).

---

## 🧪 Testes

Para rodar os testes automatizados:
```bash
PYTHONPATH=./src python -m unittest tests/teste_processamento.py
```

---

## 🖼️ Demonstração

>
> ![Exemplo de Dashboard](caminho/para/seu/print.png)

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Abra uma issue ou envie um pull request para sugerir melhorias.

---

## 📄 Licença

Este projeto está sob a licença MIT.  
Veja o arquivo LICENSE para mais detalhes.