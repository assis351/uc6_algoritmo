# Criando a lista com 4 nomes
nomes = ["Ana", "Bruno", "Carlos", "Diana"]

# Mostrando a lista inicial
print("Lista inicial:", nomes)

# Pedindo um nome ao usuário
nome_remover = input("Digite um nome para remover: ")

# Verificando se o nome existe na lista
if nome_remover in nomes:
    nomes.remove(nome_remover)
    print("Nome removido com sucesso!")
else:
    print("nome não encontrado")

# Mostrando a lista final
print("Lista final:", nomes)