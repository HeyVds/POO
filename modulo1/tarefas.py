def gerenciador_tarefas(tarefas):
  print ("\nBem vindo ao gerenciador de tarefas, abaixo você terá um menu com as opções de ações.")
  while True:
    menu = input("""
    Escolha uma das opções abaixo:
    1 - Adicionar tarefa
    2 - Marcar tarefa como concluída
    3 - Ver todas as tarefas
    0 - Voltar
    
    """)
    match menu:
      case "1":
        titulo = input("\nQual a tarefa: ").title()
        desc = input("Qual a descrição: ").title()
        status = False
        print (cadastrar_tarefa(titulo, desc, status, tarefas))
      case "2":
        tarefas_pendentes(tarefas)
        print(status_tarefa(tarefas))
        
      case "3":
        mostrar_tarefas(tarefas)
      case "0":
        print ("Encerrando...")
        break
      case _:
        print("Digite uma opção válida!")

def cadastrar_tarefa(titulo, desc, status, tarefas): #Função para adicionart uma nova tarefa com todos os campos
  if titulo not in tarefas:
    tarefas[titulo]=[desc, status]
    return "Tarefa cadastrada com sucesso!"
  else:
    return "Tarefa já existe"
  
def status_tarefa(tarefas): #Função para mudar o status da tarefa
  while True:
    sub_menu = input("Qual tarefa acima quer marcar como concluída: ").title()
    if sub_menu not in tarefas:
      print("\nDigite uma tarefa válida!")
    else:
      tarefas[sub_menu][1]=True
      return("\nTarefa marcada como concluída!")

def mostrar_tarefas(tarefas): #Função geral para exibir as tarefas
    print("*"*15,"Início da lista","*"*15)
    tarefas_pendentes(tarefas)
    tarefas_concluidas(tarefas)
    print("*"*7,"Fim da lista","*"*7)

def tarefas_pendentes(tarefas): #Função para exibir tarefas não concluídas
  print("="*10,"Lista de tarefas pendentes","="*10)
  for tarefa, lista in tarefas.items():
    if lista[1] == False:
      print(f"""
  Título: {tarefa}
  Descrição: {lista[0]}
  Status: PENDENTE
  """)

def tarefas_concluidas(tarefas): #Função para exibir tarefas concluídas
  print("="*10,"Lista de tarefas concluídas","="*10)
  for tarefa, lista in tarefas.items():
    if lista[1] == True:
      print(f"""
  Título: {tarefa}
  Descrição: {lista[0]}
  Status: CONCLUÍDA
  """)