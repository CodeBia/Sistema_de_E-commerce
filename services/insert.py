from conexao import conectar
from mysql.connector import Error

# Solicitar ao usuário os valores para serem inseridos na tabela
def inserir(conexao, cursor):
 # Criando um dicionário para adicionar os valores
    valores = {
    'cpf': None,
    'nome': None,
    'endereco': None,
    'email': None
    }

    valor = []

    valores['cpf'] = int(input("Digite o CPF: "))
    valores['nome'] = input("Diga o seu nome: ")
    valores['endereco'] = input("Informe seu endereço: ")
    valores ['email'] = input("Digite seu E-mail: ")
    valor.append(registro.copy())

    sql = "INSERT IGNORE INTO clientes (cpf, nome, endereco, email) VALUES (%s, %s, %s, %s)"
    registro = (valores['cpf'], valores['nome'], valores['endereco'], valores['email'] )
    cursor.execute(sql, registro)
    conexao.commit()

    # Mensagem ao adicionar
    if not valores:
        print("Dados não adicionados. Tente novamente")
    else: 
        print("Valores Inseridos com sucesso!")
        


    

