saldo_conta = 0
valor_deposito = 0
saques_realizados = []
depositos_realizados = []
cont_saques = -1
cont_depositos = -1

while(True):

    print("------ MENU ------ "
        "\n[S] Sacar "
        "\n[D] Depositar "
        "\n[V] Visualizar Extrato "
        "\n[E] Encerrar")

    opc = input("Digite o que deseja fazer: ").upper()

    if opc == "S":
        if cont_saques == 2:
            print("Você atingiu o limite permitido de saques. Tente novamente amanhã.")
        else: 
            valor_sacado = float(input("Insira o valor que deseja sacar: "))
        
            if valor_sacado > 500.0:
                print("Você não pode sacar valores acima de R$500,00")
            else:
                
                if valor_sacado > saldo_conta:
                    print("Não será possivel sacar o dinheiro por falta de saldo.")
                else:
                    saldo_conta -= valor_sacado
                    cont_saques += 1
                    saques_realizados.append(valor_sacado)
                    print("Saque efetuado", cont_saques)
   
    elif opc == "D":
        
        valor_deposito = float(input("Insira o valor que deseja depositar: "))

        if valor_deposito < 0:
            
            print("Por favor, deposite apenas valores acima de 0")
        
        else:

            saldo_conta += valor_deposito
            cont_depositos += 1
            depositos_realizados.append(valor_deposito)    
            print("Deposito efetuado")

    elif opc == "V":
        
        if cont_saques == -1 and cont_depositos == -1:
            print("Não foram realizadas movimentações")
        
        elif cont_saques == -1 and cont_depositos > -1:
            for valor in depositos_realizados:
                print(f"Deposito: {valor:.2f}")
       
        elif cont_saques > -1 and cont_depositos == -1:
            for valor in saques_realizados:
                print(f"Saque: {saques_realizados:.2f}")
       
        else:
            for valor in depositos_realizados:
                print(f"Deposito: {valor:.2f}")
            for valor in saques_realizados:
                print(f"Saque: {valor:.2f}")
          
        print(f"Saldo atual: {saldo_conta:.2f}")
    elif opc == "E":
        break
    else:
        print(f"Essa opção é inválida. Tente novamente!")