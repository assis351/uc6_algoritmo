#Exercicio 01 ----------------------------------------------------------------------------------

# Criando um dicionário com dados digitados pelo usuário

# Pedindo os VALORES do usuario
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

# Criando o dicionário para armazenamento
chaves = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

# Mostrando os resultados dos dados no dicionário
print("Dados cadastrados:")
print(chaves)

for chave, valor in chaves.items():
    print(chave ,":", valor)
    
#Exercicio 02 -------------------------------------------------------------------------------

# Pedindo os VALORES do usuario
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))
nota5 = float(input("Digite a nota 5: "))

# Criando o dicionário para armazenamento
aluno = {
    "nome": nome,
    "nota1": nota1,
    "nota2": nota2,
    "nota3": nota3,
    "nota4": nota4,
    "nota5": nota5
}

# Calculando a média das notas
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Mostrando os resultados dos valores e da média
print("Dados do aluno:")
for chave, valor in aluno.items():
    print(chave,":",valor)

print(f"Média do aluno: {media:.2f}")

#-----------------------------------------------------------------------------------------------