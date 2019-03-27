from random import random, uniform, randint, randrange, choice
import math

TURMAS_PEQUENAS = 25
TURMAS_GRANDES = 50
TURNO = {
    'M' : 1,
    'T' : 2,
    'N' : 3
}
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
        self.aptidao_sala = 0
        self.aptidao_horario = 0

    @staticmethod
    def lista_de_disciplinas(quantidade):
        lista = []
        for numero in range(quantidade):
            if numero < 5:
                lista.append(
                    Disciplina(numero, TURMAS_PEQUENAS, TURNO['M']) #5 turmas pequenas no turno manha
                )
            elif numero < 10:
                lista.append(
                    Disciplina(numero, TURMAS_PEQUENAS, TURNO['T']) #5 turmas pequenas no turno da tarde
                )
            elif numero < 15:
                lista.append(
                    Disciplina(numero, TURMAS_GRANDES, TURNO['M']) #5 turmas grandes no turno da manha
                )
            else:
                lista.append(
                    Disciplina(numero, TURMAS_GRANDES, TURNO['N']) #5 turmas grandes pela noite
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
                discplina.horario = randint(1, 8)
            populacao.append(Cromossomos(lista))
        return populacao

class AlgoritmoGenetico(object):
    @staticmethod
    def aptidao(cromossomo):
        def aptidao_sala(sala, tamanho):
            if (sala <= 5 and tamanho <= TURMAS_PEQUENAS) or (sala > 5 and tamanho > TURMAS_PEQUENAS):
                return 3
            elif sala > 5 and tamanho <= TURMAS_PEQUENAS:
                return 2 
            else:
                return 1

        def aptidao_horario(turno, horario):
            if (turno = 1 and 1 <= horario <= 3) or (turno = 2 and 4 <= horario <= 6) or (turno = 3 and 7 <= horario):
                return 2
            else:
                return 1

        for disciplina in cromossomo.lista:
            disciplina.aptidao_sala = aptidao_sala(disciplina.sala, disciplina.tamanho)
            disciplina.aptidao_horario = aptidao_horario(disciplina.turno, disciplina.horario)

    @staticmethod
    def avaliacao(cromossomo):
        for disciplina in cromossomo:
            if disciplina.aptidao_sala == 1 or disciplina.aptidao_horario ==1:
                return False, cromossomo
        return True, cromossomo

    @staticmethod
    def selecao(cromossomo):
        pass

    @staticmethod
    def cruzamento(cromossomo):
        pass

    @staticmethod
    def mutacao(cromossomo):
        pass



        
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
