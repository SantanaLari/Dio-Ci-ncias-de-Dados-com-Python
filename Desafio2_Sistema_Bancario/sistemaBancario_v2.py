from time import sleep

contas = []
conta_corrente = []
contador = 0
conta_corrente_por_cpf = {}

#funcao que armazena uma conta corrente em um cpf chave
def armazena_conta_corrente(agencia, numero_conta, usuario):

    for agencia, numero_conta, usuario in conta_corrente:
        if usuario in conta_corrente_por_cpf:
            conta_corrente_por_cpf[usuario].add(numero_conta)
        else:
            conta_corrente_por_cpf[usuario] = {numero_conta}

#funcao que verifica se o cpf foi encontrado
def busca_cpf(contas, cpf):
    nome = None
    for busca in contas:
        if cpf in busca[2]:
            nome = busca[0]
            break

    return nome
    
#funcao que cria um usuario e salva ele na lista contas
def criar_usuario(contas):    
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    cpf = input("Digite seu CPF: ")
    logradouro = input("Digite o seu logradouro: ")
    nro = int(input("Numero da casa: ")) 
    cidade = input("Cidade: ")
    sigla = input("Sigla: ")

    verifica_cpf = busca_cpf(contas, cpf)
    if verifica_cpf == None:
        contas.append([nome, data_nascimento, cpf, [logradouro, nro,
        cidade, sigla]])
        print("Sua conta foi criada com sucesso!")
    else:
        print("Esse CPF ja foi cadastrado")

#funcao que cria a conta corrente de um usuario que se cadastrou
def gerar_conta_corrente(contas, cpf, conta_corrente, contador):

    nome_cliente = busca_cpf(contas, cpf)

    print(f"""
Bem-vindo, {nome_cliente}!
Iremos criar uma conta corrente para voce poder
sacar, depositar e visualizar seu extrato
    """)
    print("Aguarde enquanto criamos sua conta")
    sleep(2)
    agencia = "0001"
    numero_conta = contador
    usuario = cpf
    print(f"""
Conta corrente criada, {nome_cliente}. Confira seus dados:
Agencia: {agencia}
Conta: {numero_conta}
usuario: {usuario}     
    """)
    conta_corrente.append([agencia, numero_conta, usuario])
    armazena_conta_corrente(agencia, numero_conta, usuario)

#funcao que permite que o usuario escolha a conta corrente que deseja realizar as operações
def escolha_conta_corrente(usuario, conta_corrente_por_cpf):
        
        if usuario in conta_corrente_por_cpf:
           qtd_conta_corrente = len(conta_corrente_por_cpf[usuario])
    
        if qtd_conta_corrente == 1:
            res = conta_corrente_por_cpf[usuario]
        else:
            print("Detectamos mais de uma conta corrente no seu CPF. "
                  "\nEscolha qual conta você quer usar: ", conta_corrente_por_cpf[usuario])
            opc = int(input("Digite: "))

            if opc in conta_corrente_por_cpf[usuario]:
                res = opc 
            else:
                res = next(iter(conta_corrente_por_cpf[usuario]))
                print("Essa não é uma opção válida. Por padrão estaremos te enviando para uma conta corrente válida.")      

        return res

#funcao que permite que o usuario saque, deposite e visualize o extrato
def acesso_conta(contas, senha, conta_corrente_por_cpf):

    num_conta = escolha_conta_corrente(senha, conta_corrente_por_cpf)

    saldo = 0
    limite = 500
    extrato = ""
    LIMITE_SAQUES = 3
    numero_saque = 1

    nome_cliente = busca_cpf(contas, cpf)

    while(True):
        print(f""" 
Agência: 0001 | Conta: {num_conta}
----------------------------------
Bem-vindo(a), {nome_cliente}!
O que deseja fazer?
\n[S] Saque
\n[D] Deposito
\n[E] Extrato
\n[F] Fechar  
        """)

        opcao = input("Digite sua opcao: ").upper()
        
        if opcao == "S":
            valor = float(input("Digite o valor de saque: "))
            saldo, extrato, numero_saque = saque(saldo=saldo, valor=valor, extrato=extrato, 
            limite=limite, numero_saque=numero_saque, limite_saques=LIMITE_SAQUES)
        elif opcao == "D":
            valor = float(input("Digite o valor de deposito: "))
            saldo, extrato = deposito(saldo, valor, extrato) 
        elif opcao == "E":
            extrato_visualizar(saldo, extrato=extrato)
        elif opcao == "F":
            break
        else:
            print("O sistema não reconhece essa opção. Tente novamente.")

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    
    if valor < saldo:
        if valor <= limite:
            if numero_saque <= limite_saques:
                numero_saque += 1
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                print(f"Saque de: R${valor:.2f} realizado com sucesso!")
                print(numero_saque)
            else: 
                print("Saque negado! Você atingiu o limite permitido")
        if valor > limite:
            print("Seu limite não permite que você retire esse valor.")
    else:
        print("Você não tem saldo suficiente!")
    
    return saldo, extrato, numero_saque


#deposito
def deposito(saldo, valor, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido.")

    return saldo, extrato

#extrato
def extrato_visualizar(saldo, /, *, extrato):
    print("Saldo atual: ", saldo)
    print(extrato)

while(True):

    print("---------- Bem-Vindo, Sr(a) ----------"
          "\n[C] Criar Conta"
          "\n[E] Entrar "
          "\n[G] Gerar conta corrente"
          "\n[S] Sair")

    opcao = input("Digite sua escolha: ").upper()

    if opcao == "C":
        criar_usuario(contas) 
    elif opcao == "E":
        cpf = input("Digite seu CPF: ")
        if len(conta_corrente) < 1:
            print("Crie uma conta corrente para poder ter acesso ao saque, extrato e deposito.")
        else:
            if cpf in conta_corrente_por_cpf:    
                acesso_conta(contas, cpf, conta_corrente_por_cpf)
            else: 
                print("Você não tem conta corrente. Gere uma e tenha acesso ao saque, extrato e deposito.")
    elif opcao == "G":
        cpf = input("Digite seu CPF: ")
        cpf_cadastrado = busca_cpf(contas, cpf)
        if cpf_cadastrado != None:
            contador += 1
            gerar_conta_corrente(contas, cpf, conta_corrente, contador)
        else:
            print("Essa senha nao esta cadastrada no nosso sistema.")
    
    elif opcao == "S":
        break
    else:
        print("O sistema nao reconhece essa opcao. Tente novamente")

