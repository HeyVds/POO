from cartao_web import CartaoWeb

class DiaDosNamorados(CartaoWeb):
  def __init__(self, destinatario: str):
      super().__init__(destinatario)

  def showMessage(self):
    print(f"""
      Feliz Dia dos Namorados, {self.destinatario}!
      Com carinho e muito amor!
      """)

class Natal(CartaoWeb):
  def __init__(self, destinatario: str):
      super().__init__(destinatario)

  def showMessage(self):
    print(f"""
      Feliz Natal, {self.destinatario}!
      Que sua ceia seja recheada de alegria!
      """)

class Aniversario(CartaoWeb):
  def __init__(self, destinatario: str):
    super().__init__(destinatario)

  def showMessage(self):
    print(f"""
      Parabéns, {self.destinatario}!
      Muita saúde, sucesso e realizações no seu novo ciclo!
      """)
