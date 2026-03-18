import pandas as pd


print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Criar")
print("         2 > Adicionar")
print("         3 > Apagar")
opcao = int(input("R: "))


if opcao == 1:
    print("Opção 1 selecionada")
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    dados = {
        "nome": [nome],
        "idade": [idade],
        "altura": [altura]
    }

    excel = pd.DataFrame(dados)

    excel.to_excel("Aula12\Alunos.xlsx", index=False)
    print("Ação Finalizada....")

elif opcao == 2:
    print("Opção 2 selecionada...")
    print("Para a proxima aula")