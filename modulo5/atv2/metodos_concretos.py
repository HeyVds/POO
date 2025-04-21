from metodo_pagamento import MetodoPagamento

class CartaoCredito(MetodoPagamento):
  def pagar(self):
    taxa = self.valor * 0.05
    total = self.valor + taxa
    print(f"\n[Pagamento com Cartão de Crédito]")
    print(f"Valor original: R${self.valor:.2f}")
    print(f"Taxa: R${taxa:.2f}")
    print(f"Total a pagar: R${total:.2f}")

class BoletoBancario(MetodoPagamento):
  def pagar(self):
    desconto = self.valor * 0.02
    total = self.valor - desconto
    print(f"\n[Pagamento com Boleto Bancário]")
    print(f"Valor original: R${self.valor:.2f}")
    print(f"Desconto: R${desconto:.2f}")
    print(f"Total a pagar: R${total:.2f}")

class Pix(MetodoPagamento):
  def pagar(self):
    print(f"\n[Pagamento com Pix]")
    print(f"Valor original e final: R${self.valor:.2f}")
