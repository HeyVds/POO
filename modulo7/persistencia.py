import datetime
from abc import ABC, abstractmethod

class Pessoa(ABC):
  def __init__(self, nome, cpf, data_nascimento):
    self.nome = nome
    self.__cpf = cpf
    self.data_nascimento = data_nascimento

  @abstractmethod
  def exibir_dados(self):
    pass

class Disciplina:
  def __init__(self, codigo, nome, professor_responsavel=None):
    self.codigo = codigo
    self.nome = nome
    self.professor_responsavel = professor_responsavel
    self.alunos_matriculados = []

  def exibir_dados(self):
    print(f"Disciplina: {self.nome} ({self.codigo})")
    if self.professor_responsavel:
      print(f"Professor responsável: {self.professor_responsavel.nome}")
      print("Alunos matriculados:")
    for aluno in self.alunos_matriculados:
      print(f"- {aluno.nome}")

class Aluno(Pessoa):
  def __init__(self, nome, cpf, data_nascimento, matricula):
    super().__init__(nome, cpf, data_nascimento)
    self.__matricula = matricula
    self.__notas = []
    self.disciplinas = []

  def adicionar_notas(self, notas):
    self.__notas = list(map(float, notas))

  def exibir_dados(self):
    print(f"Aluno: {self.nome} - Matrícula: {self.__matricula}")
    print(f"Disciplinas: {[d.nome for d in self.disciplinas]}")
    print(f"Notas: {self.__notas}")

class Professor(Pessoa):
  def __init__(self, nome, cpf, data_nascimento, siape):
    super().__init__(nome, cpf, data_nascimento)
    self.__siape = siape
    self.disciplinas = []

  def exibir_dados(self):
    print(f"Professor: {self.nome} - SIAPE: {self.__siape}")
    print("Disciplinas:")
    for d in self.disciplinas:
        print(f"- {d.nome}")

professores_dict = {}
alunos_dict = {}
disciplinas_dict = {}

try:
  with open("professores.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            siape, nome, cpf, data_nascimento, disciplinas_str = linha.split("|")
            data = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            professor = Professor(nome, cpf, data, siape)
            professores_dict[cpf] = professor
            professor.disciplinas_temporarias = disciplinas_str.split(",")
except FileNotFoundError:
    print("Erro: Arquivo 'professores.txt' não encontrado.")
except ValueError as e:
    print(f"Erro de leitura em 'professores.txt': {e}")

try:
  with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      linha = linha.strip()
      if linha:
        nome, cpf, data_nascimento, matricula, disciplinas_str = linha.split("|")
        data = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        aluno = Aluno(nome, cpf, data, matricula)
        alunos_dict[cpf] = aluno
        aluno.disciplinas_temporarias = disciplinas_str.split(",")
except FileNotFoundError:
    print("Erro: Arquivo 'alunos.txt' não encontrado.")
except ValueError as e:
    print(f"Erro de leitura em 'alunos.txt': {e}")

try:
  with open("disciplinas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
      linha = linha.strip()
      if linha:
        codigo, nome, cpf_prof, alunos_cpfs_str = linha.split("|")
        professor = professores_dict.get(cpf_prof)
        disciplina = Disciplina(codigo, nome, professor)
        disciplinas_dict[codigo] = disciplina
        if professor:
          professor.disciplinas.append(disciplina)
        for cpf_aluno in alunos_cpfs_str.split(","):
          aluno = alunos_dict.get(cpf_aluno)
          if aluno:
            disciplina.alunos_matriculados.append(aluno)
            aluno.disciplinas.append(disciplina)
            
except FileNotFoundError:
  print("Erro: Arquivo 'disciplinas.txt' não encontrado.")
except ValueError as e:
  print(f"Erro de leitura em 'disciplinas.txt': {e}")

print("\n--- Professores ---")
for p in professores_dict.values():
  p.exibir_dados()

print("\n--- Alunos ---")
for a in alunos_dict.values():
  a.exibir_dados()

print("\n--- Disciplinas ---")
for d in disciplinas_dict.values():
  d.exibir_dados()
