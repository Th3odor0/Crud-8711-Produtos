import os
import mysql.connector
from dotenv import load_dotenv, find_dotenv

# Encontra o arquivo .env automaticamente na estrutura de pastas
load_dotenv(find_dotenv())

class Database:

    def conectar(self):
        # Garante fallback para '127.0.0.1' e porta 3306 caso o .env não seja lido
        host = os.getenv("DB_HOST") or "127.0.0.1"
        port_env = os.getenv("DB_PORT")
        port = int(port_env) if port_env and port_env.isdigit() else 3306

        return mysql.connector.connect(
            host=host,
            port=port,
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
    
    def desconectar(self, cursor=None, conexao=None):
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()