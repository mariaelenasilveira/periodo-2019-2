from random import random, uniform, randint, randrange, choice
import math

TURMAS_PEQUENAS = 25
TURMAS_GRANDES = 50
HORARIO = {
    'M12': 1,
    'M34': 2,
    'M56': 3,
    'T12': 4,
    'T34': 5,
    'T56': 6,
    'N12': 7,
    'N34': 8
}
QUANTITADE_DISCIPLINA = 20
TAMANHO_POPULACAO = 8


class Disciplina(object):

    #O id, tamanho e turno de cada discplina é fixo.
    #horário e sala irão variar com as iteraçoes
    def __init__(self, id_disciplina=0, tamanho=0, turno=0):
        self.id_disciplina = id_disciplina
        self.tamanho = tamanho
        self.turno = turno
        self.horario = 0
        self.sala = 0

    @staticmethod
    def lista_de_disciplinas(quantidade):
        lista = []
        for numero in range(quantidade):
            if numero < 5:
                lista.append(
                    Disciplina(numero, TURMAS_PEQUENAS, HORARIO['M12']) #5 turmas pequenas no turno manha
                )
            elif numero < 10:
                lista.append(
                    Disciplina(numero, TURMAS_PEQUENAS, HORARIO['T12']) #5 turmas pequenas no turno da tarde
                )
            elif numero < 15:
                lista.append(
                    Disciplina(numero, TURMAS_GRANDES, HORARIO['M12']) #5 turmas grandes no turno da manha
                )
            else:
                lista.append(
                    Disciplina(numero, TURMAS_GRANDES, HORARIO['N12']) #5 turmas grandes pela noite
                )

        return lista

    @staticmethod
    def lista_de_disciplinas_random(quantidade):
        lista = []
        for numero in range(quantidade):
            horarios = list(HORARIO.keys())
            turmas = [TURMAS_GRANDES, TURMAS_PEQUENAS]
            turma_aleatoria = choice(turmas)
            horario_aleatorio = HORARIO[choice(horarios)]
            lista.append(
                Disciplina(numero, turma_aleatoria, horario_aleatorio)
            )
        return lista


class Cromossomos(object):
    def __init__(self, lista_de_disciplinas):
        self.lista = lista_de_disciplinas

    def populacao_inicial(self, tamanho_populacao):
        populacao = []
        for numero in range(tamanho_populacao):
            for discplina in self.lista:
                discplina.sala = randint(1, 10)
                # print(discplina.sala)
                discplina.horario = randint(1, 8)
            populacao.append(Cromossomos(lista))
            # print(populacao[numero])
        return populacao

        
lista = Disciplina.lista_de_disciplinas(QUANTITADE_DISCIPLINA)
cromossomos = Cromossomos(lista)
pop_inicial = cromossomos.populacao_inicial(TAMANHO_POPULACAO)
pop_amostral = pop_inicial[0]

for discplina in pop_amostral.lista:
    print("id: ", discplina.id_disciplina)
    print("tamanho: ", discplina.tamanho)
    print("turno: ", discplina.turno)
    print("horario: ", discplina.horario)
    print("sala: ", discplina.sala)
    print("*"*50)