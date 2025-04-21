from metodos_concretos import CartaoCredito, BoletoBancario, Pix

print("=== SISTEMA DE PAGAMENTO ===\n")
valor = float(input("Informe o valor da compra: R$"))

while True:
  print("\nEscolha o método de pagamento:")
  print("1 - Cartão de Crédito (5% de taxa)")
  print("2 - Boleto Bancário (2% de desconto)")
  print("3 - Pix (sem taxas)")

  opcao = input("Digite a opção (1/2/3): ")

  match opcao:
    case "1":
      pagamento = CartaoCredito(valor)
      break
    
    case "2":
      pagamento = BoletoBancario(valor)
      break
    
    case "3":
      pagamento = Pix(valor)
      break

    case _:
      print("Opção inválida!\n")

pagamento.pagar()

# Como o uso de polimorfismo facilitou a implementação do sistema de pagamento?
# O uso de polimorfismo permitiu resolver diferentes formas de pagamento com
# uma única referência. Mesmo que cada classe implemente o método pagar() de
# maneira distinta, todas são tratadas como um tipo comum. Isso facilita a manutenção
# e expansão do sistema, pois não é necessário reescrever código para cada novo tipo de pagamento.

# Quais seriam as vantagens de usar uma interface abstrata nesse contexto realista?
# A interface abstrata (classe MetodoPagamento) garante que todas as formas de pagamento
# tenham um comportamento obrigatório (método pagar). Isso traz segurança para o código,
# já que qualquer nova forma de pagamento precisa implementar esse método. Também ajuda
# na padronização, organização e facilita testes e integração com outros sistemas.