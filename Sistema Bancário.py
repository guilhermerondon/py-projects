# Sistema Bancário Simples

menu = """
========= MENU =========

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=======================
=> """

# Variáveis principais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado deve ser positivo.")
        except ValueError:
            print("Valor inválido! Digite apenas números.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Saldo insuficiente.")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques diários atingido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado deve ser positivo.")
        except ValueError:
            print("Valor inválido! Digite apenas números.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema. Até logo!")
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.")