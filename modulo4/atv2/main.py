from restaurante import Restaurante

restaurante1 = Restaurante("Sabor da Terra", "Comida Mineira")
restaurante2 = Restaurante("Sushi Zen", "Japonesa")
restaurante3 = Restaurante("Pizza Master", "Italiana")

print("\n--- INFORMAÇÕES DOS RESTAURANTES ---")
print(restaurante1)
print(restaurante2)
print(restaurante3)

restaurante1.abrir_restaurante()

restaurante = Restaurante("Casa do Sabor", "Brasileira")
print("\nNúmero de clientes atendidos:", restaurante.get_numero_servidos())

restaurante.set_numero_servidos(25)
print("Novo número de clientes atendidos:", restaurante.get_numero_servidos())

restaurante.incremente_numero_servidos(10)
print("Clientes atendidos após incremento:", restaurante.get_numero_servidos())
