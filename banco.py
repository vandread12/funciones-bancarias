import textwrap

def menu():
    menu = """\n
    [d]\tDepositar
    [s]\tSacar
    [e]\tExibir extrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
     >>>"""
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido!")
    return saldo,extrato


def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    if valor > 0:
        if saldo + limite >= valor:
            if numero_saques < limite_saques:
                saldo -= valor
                extrato += f"Saque: R$ {valor}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
            else:
                print("Limite de saques diários atingido!")
        else:
            print("Saldo insuficiente!")
    else:
        print("Valor inválido!")
    return saldo,extrato,numero_saques

def exibir_extrato(saldo, /,*,extrato):
    print("Extrato")
    print("Saldo: R$ 100,00")


def criar_usuario(usuarios):
    print("Criar conta")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    usuarios.append({"nome": nome, "cpf": cpf, "senha": senha})
    print("Conta criada com sucesso!")
    return usuarios

def filtrar_usuario(usuarios, cpf, senha):
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    print("Criar conta")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    usuario = filtrar_usuario(usuarios, cpf, senha)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("CPF ou senha inválidos!")
        return None

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']} Conta: {conta['numero_conta']}")
        return contas
    
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = "0001"
    numero_conta = 1

    while True:
        opcao = menu()
        if opcao == "d":
            valor = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nc":
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "q":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

