from random import random,uniform,randint,randrange
import math


class Disciplina:

	#O id, tamanho e turno de cada discplina é fixo.
	#horário e sala irão variar com as iteraçoes
	def __init__(self, id_disciplina = 0, tamanho = 0, turno = 0):
		self.id_disciplina = id_disciplina
		self.tamanho = tamanho
		self.turno = turno
		self.horario = 0
		self.sala = 0

	def lista_de_disciplinas(self, quantidade):

		lista = []
		for i in range(quantidade): #supondo inicialemente 20 turmas
			if i < 5:
				disc = Disciplina(i, 25, 10) #5 turmas pequenas no turno manha
				lista.append(disc)
			elif i < 10:
				disc = Disciplina(i, 25, 20) #5 turmas pequenas no turno da tarde
				lista.append(disc)
			elif i < 15:
				disc = Disciplina(i, 50, 10) #5 turmas grandes no turno da manha
				lista.append(disc)
			else:
				disc = Disciplina(i, 50, 30) #5 turmas grandes pela noite
				lista.append(disc)

		return lista


class Cromossomos:
	"""docstring for Cromossomos"""
	def __init__(self, lista_de_disciplinas):
		self.lista = lista_de_disciplinas

	def populacao_inicial(self, tamanho_populacao):
		
		populacao = []
		for i in range(tamanho_populacao):
			for x in self.lista:
				x.sala = randint(1,10)
				print(x.sala)
				x.horario = randint(1,30)
			populacao.append(Cromossomos(lista))
			print(populacao[i])
		return populacao

		
disciplina = Disciplina(None, None, None)
lista = disciplina.lista_de_disciplinas(20)
for i in lista:
	print("Disciplina: ", i.id_disciplina)
	print("tamanho: ", i.tamanho)
	print("turno", i.turno)
cromossomo = Cromossomos(lista)
pop_inicial = cromossomo.populacao_inicial(8)
print("id: ", pop_inicial[0].lista[0].id_disciplina)
print("tamanho: ", pop_inicial[0].lista[0].tamanho)
print("turno: ", pop_inicial[0].lista[0].turno)
print("horario: ", pop_inicial[0].lista[0].horario)
print("sala: ", pop_inicial[0].lista[0].sala)
print(" ")

print("id: ", pop_inicial[0].lista[1].id_disciplina)
print("tamanho: ", pop_inicial[0].lista[1].tamanho)
print("turno: ", pop_inicial[0].lista[1].turno)
print("horario: ", pop_inicial[0].lista[1].horario)
print("sala: ", pop_inicial[0].lista[1].sala)

