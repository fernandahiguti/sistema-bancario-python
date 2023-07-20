import re
from banking_system.models.user import User
from banking_system.models.bank_account import BankAccount

class AccountManager:
    def __init__(self):
        self.users = []
        self.accounts = []
        self.current_user = None

    def run(self):
        while True:
            print("\n========== BEM-VINDO AO BANCO ==========")
            print("[l]\tLogin com CPF")
            print("[c]\tCriar novo usuário")
            print("[q]\tSair")
            opcao = input("=> ").lower()

            if opcao == "l":
                self.log_in()

            elif opcao == "c":
                self.create_user()

            elif opcao == "q":
                print("Sessão encerrada. Obrigado por utilizar o nosso serviço!")
                break

            else:
                print("Opção inválida, por favor selecione uma opção válida.")

    def log_in(self):
        cpf = input("Informe o CPF (somente números): ")
        user = self.get_user_by_cpf(cpf)

        if user:
            print(f"Bem-vindo(a), {user.nome}!")
            self.current_user = user
            self.perform_operations()
        else:
            print("Usuário não encontrado. Por favor, crie um novo usuário ou verifique o CPF informado.")

    def create_user(self):
        nome = input("Informe o nome do usuário: ")

        while True:
            cpf = input("Informe o CPF do usuário (somente números): ")
            if cpf.isdigit():
                break
            print("CPF inválido! Por favor, informe apenas números.")

        user = self.get_user_by_cpf(cpf)
        if user:
            print("CPF já cadastrado.")
            return

        endereco = input("Informe o endereço do usuário: ")
        telefone = self.input_phone_number()

        user = User(nome, cpf, endereco, telefone)
        self.users.append(user)
        print(f"Usuário '{user.nome}' criado com sucesso!")

    def input_phone_number(self):
        while True:
            telefone = input("Informe o telefone do usuário (no formato (XX) XXXX-XXXX ou (XX) 9XXXX-XXXX): ")
            if self.validate_phone_number(telefone):
                return telefone
            print("Telefone inválido! Por favor, informe o número no formato correto.")

    def validate_phone_number(self, phone):
        pattern = r"\(\d{2}\) (9\d{4}|\d{4})-\d{4}$"
        return bool(re.match(pattern, phone))

    def get_user_by_cpf(self, cpf):
        return next((u for u in self.users if u.cpf == cpf), None)

    def get_account_by_user(self, user):
        return next((a for a in self.accounts if a.titular.cpf == user.cpf), None)

    def get_num_accounts(self, user):
        return sum(1 for a in self.accounts if a.titular.cpf == user.cpf)

    def perform_operations(self):
        print(f"\nBem-vindo(a), {self.current_user.nome}!")
        print("\n========== OPÇÕES DISPONÍVEIS ==========")
        print("[d]\tDepositar")
        print("[s]\tSacar")
        print("[e]\tExtrato")
        print("[nc]\tNova conta")
        print("[q]\tSair")
        
        while True:
            opcao = input("=> ").lower()

            if opcao == "d":
                self.deposit()

            elif opcao == "s":
                self.withdraw()

            elif opcao == "e":
                self.current_user.extrato()

            elif opcao == "nc":
                self.create_bank_account()

            elif opcao == "q":
                print("Sessão encerrada. Obrigado por utilizar o nosso serviço!")
                self.current_user = None
                break

            else:
                print("Opção inválida, por favor selecione uma opção válida.")

    def deposit(self):
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            account = self.get_account_by_user(self.current_user)
            if account:
                account.depositar(valor)
                account.extrato()
                print("Operação realizada com sucesso!")
            else:
                print("Você não possui uma conta bancária. Crie uma conta primeiro.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def withdraw(self):
        valor = float(input("Informe o valor do saque: "))

        account = self.get_account_by_user(self.current_user)
        if account:
            result, message = account.sacar(valor)
            if result:
                account.extrato()
                print("Operação realizada com sucesso!")
            else:
                print(message)
        else:
            print("Você não possui uma conta bancária. Crie uma conta primeiro.")

    def create_bank_account(self):
        user = self.current_user
        if self.get_num_accounts(user) >= 2:
            print("Você já possui o número máximo de contas bancárias (2).")
            return

        account = BankAccount()
        account.titular = user
        self.accounts.append(account)
        print(f"Conta bancária criada com sucesso para o usuário {user.nome}!")
