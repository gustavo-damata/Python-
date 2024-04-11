# Criar função menu

def menu():
    return"""
    
    []Escolha uma opção:
    [1]Extrato
    [2]Saque
    [3]Depósito
    [4]Pix
    [5]Criar conta
    [6]Novo usuario
    [7]Sair
    """

# Variáveis para armazenar informações da conta

saldo = 0 
limite = 500 
extrato_conta = ""
numero_saque = 0 
saques_no_dia = 3 
chave_pix = ""
criar_conta = True
novo_usuario_criado = criar_conta

# Criar função sacar

def sacar(*, saldo, valor, extrato, limite, limite_saques, numero_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente.")
    
    elif excedeu_limite:
        print("O valor do saque excede o limite!")
    
    elif excedeu_saques:
        print("Excedeu o numero de saque do dia!")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:R$ {valor:.2f}"
        numero_saques += 1
        print("Saque realizado com sucesso!")
  
    else:
        print("Operação falhou")

    return saldo, extrato

# Criar função depositar

def depositar(*, saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")
    return saldo, extrato

# Criar função exibir extrato

def extrato_conta(saldo, extrato_conta):
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("Histórico de transações:")
    print("Extrato")


# Criar função usuario

def novo_usuario():
    print("Usuario criado com sucesso!")

# Criar função conta

def criar_conta():
    print("Conta criada com sucesso!")


# Loop principal do sistema bancário

while True:
    print(menu())
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        extrato_conta(saldo, extrato_conta)
     
    elif opcao == "2":
        valor = float(input("Digite o valor a sacar: "))
        saldo, extrato_conta = sacar(saldo=saldo, valor=valor, extrato=extrato_conta, limite=limite, limite_saques=saques_no_dia, numero_saques=numero_saque)

    elif opcao == "3":
        valor = float(input("Digite o valor a depositar: "))
        saldo, extrato_conta = depositar(saldo=saldo, valor=valor, extrato=extrato_conta)
       
    elif opcao == "4":
        valor = float(input("Insira o valor do Pix: "))
        saldo += valor
        extrato_conta += f"Pix de R$ {valor:.2f}\n"
        print("Pix realizado com sucesso!")
    
    elif opcao == "5":
        criar_conta()
        print("Conta criada com sucesso!")
    
    elif opcao == "6":
        novo_usuario()
        print("Usuario cadastrado.")
    
    elif opcao == "7":
        print("Sair.")
        break

    else:
        print("Opção inválida. Tente novamente.")