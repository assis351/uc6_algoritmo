import pymysql as pySQL

# CONEXAO COM O BANCO DE DADOS
conexao = pySQL.connect(
    host="localhost",         # endereço do servidor (local = "localhost")
    user="root",              # usuário do MySQL
    password="",              # senha do MySQL
    database="bd_livrariaonline",      # banco que você já criou
    port=3306                 # porta padrão do MySQL (opcional)
)

# Cria o cursor — versão dicionário (retorna {"coluna": valor})
cursor = conexao.cursor(pySQL.cursors.DictCursor)


# ── Buscar todos os registros ───────────────
cursor.execute("SELECT * FROM clientes")
todos = cursor.fetchall()

#for cliente in todos:
    #print(cliente["nome"],"-", cliente["email"],"-", cliente["telefone"])
    
#cursor.execute("select * from cliente where id_ciente = 1")
#cliente = cursor.fetchone()
#print(cliente)

nome_busca = "Ursula%"
cursor.execute("select * from clientes where nome like %s")

resultado = cursor.fetchall()
print(resultado)