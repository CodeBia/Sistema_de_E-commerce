from conexao import conectar
from mysql.connector import Error

def inserir_produto(conexao, cursor):
    try:
        valores = ["impressora", "eletrônico", 718.25, 130]
            

        sql = """INSERT INTO produtos (nome, categoria, preco, estoque) VALUES (%s, %s, %s, %s)"""

        cursor.execute(sql, valores)

        conexao.commit()
        print("Produto inserido com sucesso!")
    except Error as e:
        print("Erro ao inserir:", e)

def inserir_cliente(conexao, cursor):
    try:
        valores = ["888.888.888-88", "Amanda", "Rua D, 28", "amanda@email.com"]

        sql = """INSERT IGNORE INTO clientes (cpf, nome, endereco, email) VALUES (%s, %s, %s, %s)"""

        cursor.execute(sql, valores)

        conexao.commit()
        print("Cliente inserido com sucesso!")
    except Error as e:
        print("Erro ao inserir cliente:", e)

def inserir_pedido(conexao, cursor):
    try:
        valores = ["888.888.888-88", 8, 1]
        
        sql = """INSERT INTO pedidos (cpf, id_produtos, quantidade) 
                    VALUES (%s, %s, %s)"""

        cursor.execute(sql, valores)
    
        conexao.commit()
        print("Pedido inserido com sucesso!")
    except Error as e:
        print("Erro ao inserir pedido:", e)

conexao, cursor = conectar()
if conexao and cursor:
    inserir_produto(conexao, cursor)
    inserir_cliente(conexao,cursor)
    inserir_pedido(conexao, cursor)
    cursor.close()
    conexao.close()
