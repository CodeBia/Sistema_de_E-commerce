from conexao import conectar

def deletar_produto(id_produto, cpf):
    conexao = None
    cursor = None
    try:
        conexao,cursor = conectar()
        cursor.execute("DELETE FROM pedidos WHERE id_produtos = %s", (id_produto,))
        cursor.execute("DELETE FROM produtos WHERE id_produtos = %s",(id_produto,))
        cursor.execute("DELETE FROM clientes WHERE cpf = %s",(cpf,))

        conexao.commit()
        if cursor.rowcount > 0:
            print("Deletado!")
        else:
            print("Não existe um produto com esse ID.")

    except Exception as erro:
        print("Erro ao deletar:", erro)

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

deletar_produto(7, "777.777.777-77")