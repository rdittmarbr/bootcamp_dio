import textwrap
import re

def menu():
    menu_text = """\n
    [nu]\tNovo usuário
    [lu]\tListar usuários
    ----------------------
    [nc]\tNova conta
    [lc]\tListar contas
    ----------------------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    ----------------------
    [x]\tSair
    => """
    return input(textwrap.dedent(menu_text))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n Operação falhou! O valor informado é inválido. ")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\n Operação falhou! Você não tem saldo suficiente. ")
    elif valor > limite:
        print("\n Operação falhou! O valor do saque excede o limite. ")
    elif numero_saques >= limite_saques:
        print("\n Operação falhou! Número máximo de saques excedido. ")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n Operação falhou! O valor informado é inválido. ")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    # Filtrando os numeros do CPF
    cpf = re.sub(r'\D', '', cpf)

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    })
    print("=== Usuário criado com sucesso! ===")

def listar_usuarios(usuarios):
    for usuario in usuarios:
        nome = usuario['nome'][:60]
        linha = f"""\
            CPF:\t{usuario['cpf']}\tNome:\t{nome}\tData de Nascimento:\t{usuario['data_nascimento']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    # Filtrando os numeros do CPF
    cpf = re.sub(r'\D', '', cpf)
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']} - \tC/C:\t{conta['numero_conta']} - Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 5
    AGENCIA = "0001"

    saldo = 0.0
    limite = 1500.0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "x":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
