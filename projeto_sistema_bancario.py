menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor_deposito = float(input("Insira o valor a ser depositado: "))
        if valor_deposito <= 0:
            print("Insira um valor maior que zero")
        else:
            saldo += valor_deposito
            extrato.append(f"Deposito de R$ {valor_deposito:.2f} realizado")
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você já alcançou o limite de saques diários.")
        else:
            valor_saque = float(input("Insira o valor a ser sacado: "))
            if valor_saque > saldo:
                print("Valor de saque é maior que o saldo atual")
            elif valor_saque > 500:
                print(f"Valor de saque ultrapassou o limite de R${limite:.2f} reais")
            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato.append(f"Saque de R$ {valor_saque:.2f} realizado")
    elif opcao == "e":
        print("Histórico de transações:")
        for registro in extrato:
            print(registro)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
