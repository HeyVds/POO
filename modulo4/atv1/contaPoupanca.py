from conta import Conta
from usuario import Usuario
from datetime import datetime as dt

class ContaPoupanca(Conta):
  def __init__(self, agencia, usuario: Usuario, data_abertura=dt.now(), saldo=0.0, rendimento=0.03):
    super().__init__(agencia=agencia, usuario=usuario, data_abertura=data_abertura, saldo=saldo)
    self.rendimento = rendimento

  def aplicar_rendimento(self):
    ganho = self.saldo * self.rendimento
    self.saldo += ganho
    return f"Rendimento de R${ganho:.2f} aplicado. Novo saldo: R${self.saldo:.2f}"

