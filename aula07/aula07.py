#Dicionarios em python

aluno = {
    #"chaves" : valor
    "nome":"Ana",
    "idade": 14 ,
    "nota" : 8.5,
    "curso": "Tecnico em informatica para internet",
    #array
    "array":[30, True, "Texto"],
    #dicionario dentro de outro dicionario 
    "endereco":{
        "cidade":"SP",
        "estado":"SP",
        "numero":"234"
    }
}

#acessando valores

#retorna nome do aluno
print(aluno["nome"])
#retorna nome do aluno
print(aluno["array"])
# acessando um campo especifico dentro de um array
print(aluno["array"][1])
#retorna endereço do aluno
print(aluno["endereco"])
#acessar apenas um unico campo do dicionario (endereço)
print(aluno["endereco"]["estado"])
#retorna idade do aluno
print(aluno["idade"])
#retorna nota do aluno
print(aluno["nota"])
#retorna curso do aluno
print(aluno["curso"])

#Alterar dados de dicionario
aluno["idade"] = 20
print(aluno["idade"])

#Alterar dados dentro de um array que esta dentro do dicionario
aluno["array"][2]=9
print(aluno["array"][2])

#Alterar dados do dicionario endereco que esta dentro do dicionario aluno
#Sempre que precisar acessar uma chave dentro de um dicionario usaremos colchetes
aluno["endereco"]["cidade"]= "São Paulo"
print(aluno["endereco"])
print(aluno["endereco"]["cidade"])

#Adicionar um novo campo
aluno["periodo"]="Noturno"
print(aluno)

#Deletar uma informacao
del aluno["idade"]
#Deletar mais de uma informação na mesma linha 
del aluno["idade"], aluno["curso"]
print(aluno)

#Percorrer um dicionario usando laco de repeticoes para retornar as chaves
for chave in aluno:
    print(chave)
    
#Percorrer um dicionario usando laco de repeticoes para retornar os valores
for valor in aluno.values():
    print(valor)
    
#Percorre um dicionario e retornar chave e valor
for chave, valor in aluno.items():
    print(chave,":", valor)