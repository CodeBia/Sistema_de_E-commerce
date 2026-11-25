# Criando uma conexão com o BD
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database= "sistema_ecommerce"
        )
        cursor = conexao.cursor()
# Criando o banco de dados (se não existir)
        cursor.execute("SHOW DATABASES LIKE 'sistema_ecommerce'")
        existe = cursor.fetchone()

        if existe:
            print("O banco de dados 'sistema_ecommerce' já existe") 
        else:
            cursor.execute("CREATE DATABASE sistema_ecommerce")
            print("Banco de dados criado com sucesso!")     

            cursor.execute("USE sistema_ecommerce") 
# Mensagem de conexão
        if conexao.is_connected(): 
            print("MySQL conectado com sucesso!")
            return conexao, cursor

    except Error as erro:
        print(f"Erro ao conectar ao MySQL {erro}")
   
    return None, None
# Vai testar se a conexão com o banco está funcionando e a encerra logo em seguida
conexao, cursor = conectar()
if conexao and cursor:
    cursor.close()
    conexao.close()
