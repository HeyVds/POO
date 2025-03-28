class Carro:
    def __init__(self, marca:str, modelo:str, ano:int, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
carro1 = Carro("Wolkswagem", "gol", 2015, "preto")
carro2 = Carro("Fiat", "uno", 1998, "prata")

print(f"Marca: {carro1.marca}, Modelo: {carro1.modelo}, Ano: {carro1.ano}, Cor: {carro1.cor}")
print(f"Marca: {carro2.marca}, Modelo: {carro2.modelo}, Ano: {carro2.ano}, Cor: {carro2.cor}")