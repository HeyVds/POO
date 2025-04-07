class Restaurante:
  def __init__(self, nome_restaurante, tipo_cozinha):
    self.nome_restaurante = nome_restaurante
    self.tipo_cozinha = tipo_cozinha

  def abrir_restaurante(self):
    print(f"\n{self.nome_restaurante} está agora aberto!")

  def __str__(self):
    return f"\nRestaurante: {self.nome_restaurante}\nTipo de Cozinha: {self.tipo_cozinha}"