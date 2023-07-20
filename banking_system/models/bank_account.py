import datetime

class BankAccount:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato_list = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.cheque_especial = 100

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato_list.append((datetime.datetime.now(), f"Depósito: R$ {valor:.2f}"))

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo + self.cheque_especial
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if valor > 0:
            if excedeu_saldo:
                return False, "Operação falhou! Você não tem saldo suficiente."
            elif excedeu_limite:
                return False, "Operação falhou! O valor do saque excede o limite."
            elif excedeu_saques:
                return False, "Operação falhou! Número de saques excedido"
            else:
                self.saldo -= valor
                self.extrato_list.append((datetime.datetime.now(), f"Saque: R$ {valor:.2f}"))
                self.numero_saques += 1
                return True, "Operação realizada com sucesso!"
        else:
            return False, "Operação falhou! O valor informado é inválido."

    def extrato(self):
        print("\n============= EXTRATO =============")
        for data_hora, operacao in self.extrato_list:
            print(f"{data_hora.strftime('%d/%m/%Y %H:%M:%S')} - {operacao}")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        if self.saldo < 0:
            disponivel_cheque_especial = self.cheque_especial + self.saldo
            print(f"Cheque Especial: R$ {self.cheque_especial:.2f} (Disponível: R$ {disponivel_cheque_especial:.2f})")
        else:
            print(f"Cheque Especial: R$ {self.cheque_especial:.2f}")
        print("====================================")
