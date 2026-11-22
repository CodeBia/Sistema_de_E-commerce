# Importam o código de outros arquivos (para não precisar rescrevê-los)
from conexao import conectar
from mysql.connector import Error

# Criando função para criar as tabelas
def tabelas(conexao, cursor):
    try:
        # Usando 'SHOW DATABASES LIKE...' para sabar se existe um banco de dados com esse nome antes
        cursor.execute("SHOW TABLES LIKE 'clientes'")
        existe = cursor.fetchone()
        if existe:
            print("A tabela 'cliente' já esxiste")
        else:
            tabela1 = """CREATE TABLE IF NOT EXISTS clientes(
                cpf CHAR(14) PRIMARY KEY CHECK (CHAR_LENGTH(cpf) = 14),
                nome VARCHAR(100) NOT NULL,
                endereco VARCHAR(200) NOT NULL,
                email VARCHAR(150) NOT NULL
            )"""
            cursor.execute(tabela1)
            conexao.commit()
            print("Tabela 'cliente' criada!")

    except:
        print("Erro ao criar a tabela 'clientes'")

 # O CHECK usado para cpf, preço e estoque funciona como um filtro de segurança para que dados inválidos ou mal formatados nunca sejam gravados na tabela

    try:
        cursor.execute("SHOW TABLES LIKE 'produtos'")
        existe = cursor.fetchone()
        if existe:
            print("A tabela 'produtos' já esxiste")
        else:
            tabela2 = """CREATE TABLE IF NOT EXISTS produtos(
                id_produtos INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco NUMERIC(10, 2) NOT NULL CHECK (preco > 0),
                estoque INT NOT NULL CHECK (estoque >= 0)
            );"""
            cursor.execute(tabela2)
            conexao.commit()
            print("Tabela 'produtos' criada!")
        
    except:
        print("Erro ao criar a tabela 'produtos'")

    try:
        cursor.execute("SHOW TABLES LIKE 'pedidos'")
        existe = cursor.fetchone()
        if existe:
            print("A tabela 'pedidos' já esxiste")
        else:
            tabela3 = """CREATE TABLE IF NOT EXISTS pedidos(
                id_pedidos INT AUTO_INCREMENT PRIMARY KEY,
                cpf CHAR(14),
                id_produtos INT,
                FOREIGN KEY (cpf) REFERENCES clientes(cpf),
                FOREIGN KEY (id_produtos) REFERENCES produtos(id_produtos)
            )"""
            cursor.execute(tabela3)
            conexao.commit()
            print("Tabela 'pedidos' criada!")
        
    except:
        print("Erro ao criar a tabela 'pedidos'")
# Funciona para que as funções sejam chamadas e funcionem        
conexao, cursor = conectar()
if conexao and cursor:
    tabelas(conexao, cursor)
    cursor.close()
    conexao.close()
