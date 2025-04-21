from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
  def __init__(self, valor: float):
    self.valor = valor

  @abstractmethod
  def pagar(self):
    pass

