# BANCO Tabajara 
import pandas as pd
import os

caminho_excel = "BANCO_TABAJARA/Banco_Tabajara.xlsx"

print("====================")
print("  BANCO TABAJARA")
print("  ")
print("  Escolha uma opção")
print("  1 - Criar conta")
print("  2 - Acessar conta")
print("==================\n")
opcao = int(input("R: "))

# =========================
# CRIAR CONTA
# =========================
if opcao == 1:
    nome_cliente = input("Nome completo: ")
    cpf = int(input("CPF: "))
    tipo_conta = input("Tipo da conta (corrente/poupanca/salario): ").lower()

    if not os.path.exists(caminho_excel):

        dados = {
            "nome_cliente": [nome_cliente],
            "cpf": [cpf],
            "tipo_conta": [tipo_conta],
            "numero_conta": [0],
            "agencia": [400],
            "extrato_bancario": [0.0],
            "deposito": [0.0],
            "saque": [0.0]
        }

        df = pd.DataFrame(dados)

    else:
        df = pd.read_excel(caminho_excel)

        nova_conta = df["numero_conta"].iloc[-1] + 1
        nova_agencia = df["agencia"].iloc[-1] + 1

        nova_linha = {
            "nome_cliente": nome_cliente,
            "cpf": cpf,
            "tipo_conta": tipo_conta,
            "numero_conta": nova_conta,
            "agencia": nova_agencia,
            "extrato_bancario": 0.0,
            "deposito": 0.0,
            "saque": 0.0
        }

        df.loc[len(df)] = nova_linha

    df.to_excel(caminho_excel, index=False)

    print("\nConta criada com sucesso!")
    print("================================================")
    print(f"Nome: {nome_cliente}")
    print(f"CPF: {cpf}")
    print(f"Tipo conta: {tipo_conta}")
    print(f"Número da conta: {df.iloc[-1]['numero_conta']}")
    print(f"Agência: {df.iloc[-1]['agencia']}")
    print(f"Saldo: {df.iloc[-1]['extrato_bancario']}")
    print("================================================\n")

# =========================
# ACESSAR CONTA
# =========================
elif opcao == 2:

    cpf_input = int(input("CPF: "))
    numero_conta_input = int(input("Número da conta: "))

    if not os.path.exists(caminho_excel):
        print("Usuário não encontrado, tentar novamente ou realizar o cadastro")
        exit()

    df = pd.read_excel(caminho_excel, dtype={'extrato_bancario':float})

    conta = df[(df["cpf"] == cpf_input) & (df["numero_conta"] == numero_conta_input)]

    if conta.empty:
        print("Usuário não encontrado, tentar novamente ou realizar o cadastro")
        exit()

    index = conta.index[0]
    nome_cliente = df.loc[index, "nome_cliente"]
    saldo = float(df.loc[index, "extrato_bancario"])
    tipo_conta = df.loc[index, "tipo_conta"]
    
    print(f"\nBem-vindo {nome_cliente} ao banco Tabajara")

    # MENU
    print("====================")
    print("1 - Saque")
    print("2 - Deposito")
    print("3 - Saldo")
    print("====================")
    escolha = int(input("Escolha: "))

    # =========================
    # TAXAS (%)
    # =========================
    if tipo_conta == "corrente":
        taxa_percentual = 0.05
    elif tipo_conta == "poupanca":
        taxa_percentual = 0.0
    elif tipo_conta == "salario":
        taxa_percentual = 0.02
    else:
        taxa_percentual = 0.0

    # =========================
    # SAQUE
    # =========================
    if escolha == 1:
        valor = float(input("Digite o valor do saque: "))

        if valor > saldo:
            print("Valor maior que o disponivel em conta")
            exit()

        taxa_valor = valor * taxa_percentual
        desconto_total = valor + taxa_valor
        saldo -= desconto_total

        df.loc[index, "extrato_bancario"] = saldo
        df.loc[index, "saque"] += valor
        df.to_excel(caminho_excel, index=False)

        print("================================================")
        print("      Saque realizado com sucesso!")
        print(f"      Saque: {valor}")
        print(f"      Valor em conta: {saldo}")
        print(f"      Taxa para saque: {taxa_percentual * 100}%")
        print(f"      Valor de desconto saque: {desconto_total}")
        print("================================================\n")

    # =========================
    # DEPOSITO
    # =========================
    elif escolha == 2:
        valor = float(input("Digite o valor do depósito: "))

        if valor < 0:
            print("Numero invalido, operação encerrada")
            exit()

        saldo += valor

        df.loc[index, "extrato_bancario"] = saldo
        df.loc[index, "deposito"] += valor
        df.to_excel(caminho_excel, index=False)

        print("================================================")
        print(f"      Valor depositado: {valor}")
        print(f"      Saldo em conta: {saldo}")
        print("================================================\n")

    # =========================
    # SALDO
    # =========================
    elif escolha == 3:
        print("================================================")
        print(f"   Tipo conta: {tipo_conta}")
        print(f"   Saldo em conta: {saldo}")
        print("================================================\n")

    else:
        print("Opção inválida.")