# Criando uma conexão com o BD
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="bianquita",
            password="Popos2026@mysql"
        )
        cursor = conexao.cursor()

        cursor.execute("SHOW DATABASES LIKE 'sistema_ecommerce'")
        existe = cursor.fetchone()

        if existe:
            print("O banco de dados 'sistema_ecommerce' já existe") 
        else:
            cursor.execute("CREATE DATABASE sistema_ecommerce")
            print("Banco de dados criado com sucesso!")     

            cursor.execute("USE sistema_ecommerce") 

        if conexao.is_connected(): 
            print("MySQL conectado com sucesso!")
            return conexao, cursor

    except Error as erro:
        print(f"Erro ao conectar ao MySQL {erro}")
   
    return None, None

conexao, cursor = conectar()
if conexao and cursor:
    cursor.close()
    conexao.close()
