class Restaurante:
  def __init__(self, nome_restaurante, tipo_cozinha, numero_servidos=0):
    self.nome_restaurante = nome_restaurante
    self.tipo_cozinha = tipo_cozinha
    self.numero_servidos = numero_servidos

  def abrir_restaurante(self):
    print(f"\n{self.nome_restaurante} está agora aberto!")

  def get_numero_servidos(self):
    return self.numero_servidos

  def set_numero_servidos(self, numero):
    self.numero_servidos = numero

  def incremente_numero_servidos(self, incremento):
    novo_total = self.get_numero_servidos() + incremento
    self.set_numero_servidos(novo_total)

  def __str__(self):
    return (
      f"\nRestaurante: {self.nome_restaurante}"
      f"\nTipo de Cozinha: {self.tipo_cozinha}"
      f"\nClientes Servidos: {self.numero_servidos}"
    )
