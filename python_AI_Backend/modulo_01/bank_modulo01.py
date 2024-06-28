def exibir_menu():
    print("\nMenu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Visualizar Extrato")
    print("4. Sair")

def depositar(saldo, extrato):
    valor = float(input("Digite o valor a ser depositado: R$ "))
    if valor <= 0:
        print("Valor de depósito deve ser positivo!")
    else:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo

def sacar(saldo, extrato, saques_hoje, saques_totais):
    if saques_hoje >= saques_totais:
        print("Limite diário de saques atingido! Você só pode realizar 3 saques por dia.")
        return saldo, saques_hoje

    valor = float(input("Digite o valor a ser sacado: R$ "))
    if valor <= 0:
        print("Valor de saque deve ser positivo!")
    elif valor > 500:
        print("O valor máximo para saque é de R$ 500,00.")
    elif valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_hoje += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, saques_hoje

def visualizar_extrato(extrato, saldo):
    print("\nExtrato:")
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("\n")

def main():
    saldo   = 0.0
    extrato = []
    saques_hoje   = 0
    saques_totais = 3

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            saldo = depositar(saldo, extrato)
        elif opcao == '2':
            saldo, saques_hoje = sacar(saldo, extrato, saques_hoje, saques_totais )
        elif opcao == '3':
            visualizar_extrato(extrato, saldo)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

        print(f"\nSaldo atual: R$ {saldo:.2f}")

if __name__ == "__main__":
    main()
