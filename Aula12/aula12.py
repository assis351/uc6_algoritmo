import pandas as pd

nome = str(input("Digite seu nome: "))
idade = str(input("Digite sua idade: "))
altura = str(input("Digite sua altura: "))

dados = {
    "nome":[nome],
    "idade":[idade],
    "altura":[altura],
}

excel = pd.DataFrame(dados)

excel.to_excel("Aula12/castrado_alunos.xlsx")
