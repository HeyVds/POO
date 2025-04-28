from locadora import Veiculo

carro1 = Veiculo("ABC-1234", "Sedan", 150.0)
carro2 = Veiculo("DEF-5678", "SUV", 200.0)

print(carro1.alugar())
print(carro1.status)

print(carro1.devolver())
print(carro1.status)

print(carro1.placa)
carro1.placa = "XYZ-9999"

print(Veiculo.mostrar_total_veiculos())

dias = 5
print(f"Valor do aluguel por {dias} dias: R${Veiculo.calcular_diaria(dias, carro1.diaria)}")
