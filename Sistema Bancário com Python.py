LIMITE_SAQUES = 3
LIMITE = 500
saldo = 0
extrato = ""
numero_saques = 0
op = 0

while op != 4:
    op = str(input("\nEscolha uma operação:\n [d] - Depósito\n [s] - Saque\n [e] - Extrato\n [q] - Sair\n\n =>"))
    
    if op == "d":
        valor = float(input("Digite o valor do Deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$: {valor:.2f}\n"
        else:
            print("Operação falhou!!! O valor informado é invalido!")

    elif op.lower() == "s":
        if LIMITE_SAQUES <= numero_saques:
            print(f"Operação falhou!!! A quantidades de saques excedeu o limite de {LIMITE_SAQUES} saques")
        else:
            valor = float(input("Digite o valor do Saque: "))

            if valor > saldo:
                print("Operação falhou!!! Não há saldo o suficiente para saque!")
            
            elif valor > LIMITE:
                print(f"Operação falhou!!! O limite de saque é de {LIMITE} reais") 
            
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$: {valor:.2f}\n"
                numero_saques += 1

    elif op.lower() == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif op.lower() == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
