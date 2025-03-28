class Pessoa:
    def __init__(self, nome:str, idade:int, cidade:str):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}."
    
pessoa1 = Pessoa("Fulano", 15, "fortaleza")
pessoa2= Pessoa("Ciclano", 98, "maranguape")

print(pessoa1.apresentar())
print(pessoa2.apresentar())