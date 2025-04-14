from conta import Conta
from usuario import Usuario
from datetime import datetime as dt

class ContaCorrente(Conta):
  def __init__(self, agencia, usuario: Usuario, data_abertura=dt.now(), saldo=0, tarifa_mensal=20):
    super().__init__(agencia=agencia, usuario=usuario, data_abertura=data_abertura, saldo=saldo)
    self.tarifa_mensal = tarifa_mensal

  def cobrar_tarifa(self):
    if self.saldo >= self.tarifa_mensal:
      self.saldo -= self.tarifa_mensal
      return f"Tarifa de R${self.tarifa_mensal:.2f} cobrada com sucesso."
    else:
      return "Saldo insuficiente para cobrar a tarifa."