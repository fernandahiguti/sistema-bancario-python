import datetime

class Transaction:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo
        self.data_hora = datetime.datetime.now()

    def __str__(self):
        return f"{self.data_hora.strftime('%d/%m/%Y %H:%M:%S')} - {self.tipo}: R$ {self.valor:.2f}"
