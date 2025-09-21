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
DB_SERVER=SEU_SERVIDOR
DB_PORT=1433
DB_NAME=AdventureWorks
DB_USER=SEU_USUARIO
DB_PASSWORD=SUA_SENHA
```

## 🚀 Como Executar

Com o ambiente virtual ativado e o arquivo `.env` configurado, execute o seguinte comando a partir da pasta raiz do projeto:

```bash
streamlit run src/dashboard/app.py
```

O dashboard será aberto automaticamente no seu navegador.