def gerenciamento_alunos(alunos):
  print ("Bem vindo à escola, abaixo você terá um menu com as opções de ações.")
  while True:
    menu = input("""
  Escolha uma opção:
  1 adicionar um novo aluno e suas notas
  2 atualizar a nota de um aluno
  3 remover um aluno
  4 exibir todos os alunos
  5 exibir a média de cada aluno 
  0 Voltar
                 
  """)
    match menu:
      case "1":
        nome = input("\nDigite o nome do(a) aluno(a): ").title()
        n1 = float(input("Digite a nota 1: "))
        n2 = float(input("Digite a nota 2: "))
        n3 = float(input("Digite a nota 3: "))
        n4 = float(input("Digite a nota 4: "))
        print(cadastrar_alunos(nome, n1, n2, n3, n4, alunos))

      case "2":
        nome = input("Digite o nome do aluno: ").title()
        n = input("Qual a nota deseja alterar(n1,n2,n3,n4): ")
        nota = float(input("Digite o valor da nota: "))
        print (atualizar_nota(nome, n, nota, alunos))

      case "3":
        nome = input("Digite o nome do aluno que você deseja remover: ").title()
        print(remover_aluno(nome, alunos))

      case "4":
        exibir_alunos(alunos)
      
      case "5":
        exibir_media(alunos)

      case "0":
        print ("\nEncerrando escola...\n")
        break
      case _:
        print ("\nDigite uma opção válida!\n")

def cadastrar_alunos(nome, n1, n2, n3, n4, alunos):
  if nome in alunos:
    return "\nEste aluno já está cadastrado, caso queira alterar alguma nota use a opção 2!"
  else:
    alunos[nome]=[n1,n2,n3,n4]
    return f"\nO(a) aluno(a) {nome} foi cadastrado com sucesso!"
  
def atualizar_nota(nome, n, nota, alunos):
  if nome in alunos:
    if n == "n1":
      n = 0
    elif n == "n2":
      n = 1
    elif n == "n3":
      n = 2
    elif n == "n4":
      n = 3
    else:
      return "Nota inválida!"
    alunos[nome][n] = nota
    return "Nota do(a) aluno(a) atualizada com sucesso!"
  else:
    return ("Aluno(a) não existe!")
  
def exibir_media(alunos):
  print ("*"*8, "Lista de alunos", "*"*8)
  for aluno, notas in alunos.items():
    media = sum(notas)/len(notas)
    print(f"""
  Aluno(a): {aluno}, Média: {media}""")
  print ("="*35,"\n")

  
def remover_aluno(nome, alunos):
  if nome in alunos:
    del alunos[nome]
    return "Aluno removido com sucesso!"
  else:
    return "Aluno(a) não existe!"


def exibir_alunos(alunos):
  print ("*"*8, "Lista de alunos", "*"*8)
  for aluno, notas in alunos.items():
    print(f"""
  Aluno(a): {aluno}, notas: {notas}""")
  print ("="*35,"\n")