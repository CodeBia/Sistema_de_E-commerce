from conexao import conectar
from mysql.connector import Error

nome = "João"
idade = 17
sql = "INSERT INTO produtos (nome, categoria, preco, estoque ) VALUES (%s, %s, %s, %s)"
valores = (nome, categoria, preco, estoque)
cursor.execute(sql, valores)