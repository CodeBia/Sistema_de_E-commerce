from conexao import conectar
from mysql.connector import Error

def inserir_produto(conexao, cursor):
    try:
        nome = "sapatilha"
        categoria = "calcados"
        preco = 200.00
        estoque = 5

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
        cpf = "888.888.888-88"
        nome = "Renata"
        endereco = "Rua F, 90"
        email = "renata@email.com"

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
        cpf = "888.888.888-88"
        id_produtos = 3
        quantidade = 4

        sql = """INSERT INTO pedidos (cpf, id_produtos, quantidade)
                 VALUES (%s, %s, %s)"""
        valores = (cpf, id_produtos, quantidade)

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