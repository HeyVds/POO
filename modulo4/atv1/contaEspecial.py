from contaCorrente import ContaCorrente
from usuario import Usuario
from datetime import datetime as dt

class ContaEspecial(ContaCorrente):
  def __init__(self, agencia, usuario: Usuario, data_abertura=dt.now(), saldo=0.0, tarifa_mensal=20.0, limite=1000.0):
    super().__init__(agencia=agencia, usuario=usuario, data_abertura=data_abertura, saldo=saldo, tarifa_mensal=tarifa_mensal)
    self.limite = limite

  def consultar_saldo(self):
    return f"Saldo disponível: R${self.saldo + self.limite:.2f} (incluindo limite)"

  def sacar(self, valor):
    if self.saldo + self.limite < valor:
      return "Valor acima do limite da conta especial!"
    else:
      self.saldo -= valor
      return f"O valor R${valor:.2f} foi sacado!"

  def transferir(self, valor, usuario_destino):
    if self.saldo + self.limite < valor:
      return "Transferência acima do limite da conta especial!"
    else:
      self.saldo -= valor
      return f"O valor R${valor:.2f} foi transferido para {usuario_destino.get_nome()}!"