from abc import ABC, abstractmethod

class CartaoWeb(ABC):
  def __init__(self, destinatario: str):
    self.destinatario = destinatario

  @abstractmethod
  def showMessage(self):
    pass
