from conexao import conectar
from mysql.connector import Error


def atualizar_aluno(id_aluno, novos_dados):
    # novos_dados ex: {"nome": "Julia Santos", "curso": "Banco de Dados"}
    conexao = conectar()
    if conexao is None:
        return
    try:
        cursor = conexao.cursor()
        campos = ", ".join(f"{coluna} = %s" for coluna in novos_dados.keys())
        valores = list(novos_dados.values())
        valores.append(id_aluno)

        sql = f"UPDATE alunos SET {campos} WHERE id = %s"
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"{cursor.rowcount} linha(s) atualizada(s).")
    except Exception as erro:
        print(f"Erro: {erro}")
        conexao.rollback()
    finally:
        conexao, cursor = conectar()
        if conexao and cursor:
            atualizar_aluno (conexao, cursor)
            cursor.close()
            conexao.close()
<<<<<<< HEAD
>>>>>>> atualizacao
=======
>>>>>>> 50c05acae5d8cfe5f9372f1e3dc7e07384cb76c4
