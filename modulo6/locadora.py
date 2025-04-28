class Veiculo:
  total_veiculos = 0 
  def __init__(self, placa:str, modelo:str, diaria:float):
    self.__placa = placa
    self.modelo = modelo
    self.diaria = diaria
    self.__alugado = False
    Veiculo.total_veiculos += 1

  def alugar(self):
    if not self.__alugado:
      self.__alugado =True
      return f"Veículo: {self.modelo} de placa:{self.placa} alugador com sucesso!"
    else:
      return f"O veículo: {self.modelo} de placa:{self.placa} não está disponível!"
    
  def devolver(self):
    if self.__alugado:
      self.__alugado = False
      return f"Veículo: {self.modelo} de placa:{self.placa} devolvido com sucesso!"
    else:
      return f"O veículo: {self.modelo} de placa:{self.placa} não estava alugado!"
  
  @property
  def status(self):
    if self.__alugado:
      return "Alugado!"    
    else:
      return "Disponível!"

  @property
  def placa(self):
    return self.__placa

  @placa.setter
  def placa(self,_):
    print ("A placa não pode ser modificada!")
  
  @classmethod
  def mostrar_total_veiculos(cls):
    return f"O total de veículos cadastrados é: {Veiculo.total_veiculos}"
  
  @staticmethod
  def calcular_diaria(diaria, dias):
    return (diaria * dias)
