import banking_system as bs

def main():
    menu = """
=========== Bem-vindo(a) ===========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
====================================

=> """

    account = bs.Account()

    while True:
        opcao = input(menu)

        if opcao == "d":
            account.depositar()

        elif opcao == "s":
            account.sacar()

        elif opcao == "e":
            account.extrato()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
