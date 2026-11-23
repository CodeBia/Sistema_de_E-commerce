# Importam o código de outros arquivos (para não precisar rescrevê-los)
from conexao import conectar
from mysql.connector import Error

def listar(conexao, cursor):








# Funciona para que as funções sejam chamadas e funcionem       
conexao, cursor = conectar()
if conexao and cursor:
    tabelas(conexao, cursor)
    cursor.close()
    conexao.close()

    