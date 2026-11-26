from conexao import conectar

def atualizar_produto(conexao, cursor):
    sql = """
    UPDATE produtos
    SET preco = %s, estoque = %s
    WHERE id_produtos = %s
    """
    try:
        cursor.execute(sql, (123.90, 80, 6))
        conexao.commit()
        print("Produto atualizado com sucesso!", {cursor.rowcount})
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")

def atualizar_cliente(conexao, cursor):
    sql = """
    UPDATE clientes
    SET nome = %s, email = %s
    WHERE cpf = %s
    """
    try:
        cursor.execute(sql, ("Camila", "camila@gmail.com", "666.666.666-66"))
        conexao.commit()
        print("Cliente atualizado com sucesso!", {cursor.rowcount})
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")

# Parte principal - só aqui abre e fecha a conexão
conexao, cursor = conectar()
if conexao and cursor:
    atualizar_produto(conexao, cursor)
    atualizar_cliente(conexao, cursor)
    cursor.close()
    conexao.close()
