def estoque_produtos(produtos):
  print ("Bem vindo ao estoque, abaixo você terá um menu com as opções de ações.")
  while True:
    menu = input("""
  Escolha uma opção:
  1 adicionar um novo produto
  2 remover um produto
  3 atualizar a quantidade de um produto
  4 exibir todos os produtos no estoque
  0 Voltar
                 
  """)
    match menu:
      case "1":
        nome = input("\nDigite o nome do produto: ").title()
        qtd_produto = int(input("Digite a quantidade: "))
        print(adicionar_estoque(nome, qtd_produto, produtos))
      case "2":
        nome = input("Digite o nome do produto que você deseja deletar: ").title()
        print(deletar_produto(nome, produtos))
      case "3":
        nome = input("Digite o nome do produto que você deseja deletar: ").title()
        qtd_produto = int(input("Digite a quantidade do produto que você deseja atualizar: "))
        print(atualizar_estoque(nome, qtd_produto, produtos))

      case "4":
        exibir_produtos(produtos)
      case "0":
        print ("\nEncerrando estoque...\n")
        break
      case _:
        print ("\nDigite uma opção válida!\n")

def adicionar_estoque(produto,qtd_produto, produtos):
  if produto in produtos:
    return "\nEste produto já está cadastrado, caso queira alterar a quantidade use a opção 3!"
  else:
    produtos[produto]=qtd_produto
    return f"\nProduto {produto} foi adicionado com sucesso!"
  
def deletar_produto(produto, produtos):
  if produto in produtos:
    del produtos[produto]
    return "\nO produto foi deletado com sucesso!\n"
  else:
    return "\nEste produto não existe!"
  
def atualizar_estoque(produto, qtd_produto, produtos):
  if produto in produtos:
    produtos[produto] = qtd_produto
    return "\nA quantidade do produto foi atualziada com sucesso com sucesso!\n"
  else:
    return "Este produto não existem!"

def exibir_produtos(produtos):
  print ("*"*8, "Lista de produtos", "*"*8)
  for produto, qtd in produtos.items():
    print(f"""
    Produto: {produto}, quantidade: {qtd}""")
  print ("="*35,"\n")