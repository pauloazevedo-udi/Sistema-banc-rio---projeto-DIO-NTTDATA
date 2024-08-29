def banco():
    saldo = 0
    limite_saque = 500
    saques_diarios = 3
    numero_saques = 0
    transacoes = []

    while True:
        print("\nEscolha a operação:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: R$ "))
            if valor > 0:
                saldo += valor
                transacoes.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido. Depósitos devem ser positivos.")

        elif opcao == "2":
            if numero_saques >= saques_diarios:
                print("Limite de saques diários atingido.")
            else:
                valor = float(input("Digite o valor para saque: R$ "))
                if valor > saldo:
                    print("Saldo insuficiente para saque.")
                elif valor > limite_saque:
                    print(f"Valor excede o limite de R$ {limite_saque:.2f} por saque.")
                else:
                    saldo -= valor
                    transacoes.append(f"Saque: R$ {valor:.2f}")
                    numero_saques += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        elif opcao == "3":
            print("\nExtrato:")
            if not transacoes:
                print("Nenhuma transação realizada.")
            else:
                for transacao in transacoes:
                    print(transacao)
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    banco()
