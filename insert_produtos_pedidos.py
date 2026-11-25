from conexao import conectar
from mysql.connector import Error

def inserir_produto(conexao, cursor):
    try:
        nome = "camiseta"
        categoria = "roupas"
        preco = 49.90
        estoque = 10

        sql = """INSERT INTO produtos (nome, categoria, preco, estoque)
                 VALUES (%s, %s, %s, %s)"""
        valores = (nome, categoria, preco, estoque)

        cursor.execute(sql, valores)
        conexao.commit()
        print("Produto inserido com sucesso!")
    except Error as e:
        print("Erro ao inserir:", e)

def inserir_cliente(conexao, cursor):
    try:
        cpf = "111.111.111-11"
        nome = "jusami"
        endereco = "Rua A, 10"
        email = "jusami@email.com"

        sql = """INSERT IGNORE INTO clientes (cpf, nome, endereco, email)
                 VALUES (%s, %s, %s, %s)"""
        valores = (cpf, nome, endereco, email)

        cursor.execute(sql, valores)
        conexao.commit()
        print("Cliente inserido com sucesso!")
    except Error as e:
        print("Erro ao inserir cliente:", e)

def inserir_pedido(conexao, cursor):
    try:
        cpf = "111.111.111-11"
        id_produtos = 1
        quantidade = 2
        data_pedido = "2026-11-23"

        sql = """INSERT INTO pedidos (cpf, id_produtos, quantidade, data_pedido)
                 VALUES (%s, %s, %s, %s)"""
        valores = (cpf, id_produtos, quantidade, data_pedido)

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