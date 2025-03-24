import estoque
import escola
import tarefas
lista_tarefas = {}
produtos = {}
alunos = {
    "Ana": [8.5, 7.0, 9.2, 6.8],
    "Carlos": [5.5, 6.0, 7.5, 8.0],
    "Mariana": [9.0, 8.5, 10.0, 9.8],
    "Lucas": [6.5, 7.2, 5.8, 6.9],
    "Fernanda": [7.8, 8.2, 7.0, 8.5]
}

while True:
    menu = input("""
    Escolha uma das opções abaixo:
    1 - Estoque
    2 - Escola
    3 - Tarefas
    0 - Encerrar
    
    """)
    match menu:
      case "1":
        estoque.estoque_produtos(produtos)
      case "2":
        escola.gerenciamento_alunos(alunos)
      case "3":
        tarefas.gerenciador_tarefas(lista_tarefas)
      case "0":
        print ("Encerrando...")
        break
      case _:
        print("Digite uma opção válida!")
