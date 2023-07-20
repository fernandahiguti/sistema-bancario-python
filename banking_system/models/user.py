class User:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def extrato(self):
        print(f"\n=========== EXTRATO DE {self.nome.upper()} ===========")
        print("Não foram realizadas movimentações.\n")
        print(f"CPF: {self.cpf}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print("=====================================================\n")
