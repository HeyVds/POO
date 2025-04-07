from usuario import Usuario
from conta import Conta

usuario1 = Usuario()

nome = input("Digite o nome do usuário: ")
rg = int(input("Informe o RG do usuário: "))
cpf = int(input("Informe o CPF do usuário: "))
dia = int(input("Informe o dia de nascimento: "))
mes = int(input("Informe o mês de nascimento: "))
ano = int(input("Informe o ano de nascimento: "))

usuario1.set_nome(nome)
usuario1.set_rg(rg)
usuario1.set_cpf(cpf)
usuario1.set_data_nascimento(dia, mes, ano)

saldo = float(input("Informe o saldo inicial da conta: "))
conta1 = Conta(usuario=usuario1, saldo=saldo)

print("\n--- INFORMAÇÕES DA CONTA ---")
print(conta1)
