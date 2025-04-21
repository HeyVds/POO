from modelos_cartoes import DiaDosNamorados, Natal, Aniversario


cartao = DiaDosNamorados("Maria")
cartao.showMessage()

cartao = Natal("João")
cartao.showMessage()

cartao = Aniversario("Lucas")
cartao.showMessage()


# POLIMORFISMO:
# Polimorfismo é quando várias classes diferentes compartilham um mesmo
# método de forma distinta. Ele permite usar uma mesma interface
# para diferentes comportamentos.
#
# Neste caso, a variável 'cartao' é do tipo CartaoWeb, mas pode receber
# instâncias de subclasses diferentes. Cada uma implementa o método
# showMessage de forma personalizada. O mesmo método sendo executado
# de formas diferentes conforme o tipo real do objeto instanciado.
