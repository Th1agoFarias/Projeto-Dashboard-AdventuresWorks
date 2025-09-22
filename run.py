import subprocess


if __name__ == "__main__":
    print("Iniciando o Dashboard AdventureWorks...")
    print("Acesse: http://localhost:8501")
    print("Para parar: Ctrl+C")
    print("-" * 50)
    
    subprocess.run(["streamlit", "run", "src/app.py"])