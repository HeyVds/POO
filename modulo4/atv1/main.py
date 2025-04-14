from usuario import Usuario
from conta import Conta
from contaPoupanca import ContaPoupanca
from contaCorrente import ContaCorrente
from contaEspecial import ContaEspecial
from datetime import datetime as dt

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

saldo = float(input("Digite o saldo inicial da conta comum: "))
conta1 = Conta(usuario=usuario1, saldo=saldo)

saldo_poupanca = float(input("Digite o saldo inicial da conta poupança: "))
conta_poupanca = ContaPoupanca(agencia=101, usuario=usuario1, saldo=saldo_poupanca)

saldo_corrente = float(input("Digite o saldo inicial da conta corrente: "))
conta_corrente = ContaCorrente(agencia=102, usuario=usuario1, saldo=saldo_corrente)

saldo_especial = float(input("Digite o saldo inicial da conta especial: "))
conta_especial = ContaEspecial(agencia=103, usuario=usuario1, saldo=saldo_especial, limite=500.0)

print("\n--- INFORMAÇÕES DAS CONTAS ---")
print("\n[CONTA COMUM]\n", conta1)
print("\n[CONTA POUPANÇA]\n", conta_poupanca)
print(conta_poupanca.aplicar_rendimento())
print("\n[CONTA CORRENTE]\n", conta_corrente)
print(conta_corrente.cobrar_tarifa())
print("\n[CONTA ESPECIAL]\n", conta_especial)
print(conta_especial.consultar_saldo())
print(conta_especial.sacar(800.0))