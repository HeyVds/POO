class Livro:
    def __init__(self, titulo:str, autor:str, ano_publicacao:int, preco:float):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco
    
livro1 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, 45.50)
livro2 = Livro("1984", "George Orwell", 1949, 38.90)

print(f"Título: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano_publicacao}, Preço: R${livro1.preco}")
print(f"Título: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano_publicacao}, Preço: R${livro2.preco}")