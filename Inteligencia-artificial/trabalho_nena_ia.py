from random import random, uniform, randint, randrange, choice
import math

TURMAS_PEQUENAS = 25
TURMAS_GRANDES = 50
TURNO = {
    'M' : 1,
    'T' : 2,
    'N' : 3
}
QUANTITADE_DISCIPLINA = 20
TAMANHO_POPULACAO = 8
ITERACOES_MAX = 5

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
            if (turno == 1 and 1 <= horario <= 3) or (turno == 2 and 4 <= horario <= 6) or (turno == 3 and 7 <= horario):
                return 2
            else:
                return 1

        for disciplina in cromossomo.lista:
            disciplina.aptidao_sala = aptidao_sala(disciplina.sala, disciplina.tamanho)
            disciplina.aptidao_horario = aptidao_horario(disciplina.turno, disciplina.horario)
        return cromossomo

    @staticmethod
    def avaliacao(cromossomo):
        for disciplina in cromossomo.lista:
            if disciplina.aptidao_sala == 1 or disciplina.aptidao_horario ==1:
                return False, cromossomo
        return True, cromossomo

    @staticmethod
    def selecao(populacao):
        def torneio(cromossomo):
            soma = 0
            for disciplina in cromossomo.lista:
                soma += disciplina.aptidao_horario*disciplina.aptidao_sala
            return soma

        pares_de_cromossomos = [populacao[i:i+2] for i in range(0, len(populacao), 2)]
        cromossomos_melhores = []
        for par in pares_de_cromossomos:
            disciplina_melhor = max(par, key=torneio)
            cromossomos_melhores.append(disciplina_melhor)
        return cromossomos_melhores

    @staticmethod
    def cruzamento(populacao_selecionada):
        pares_de_cromossomos = [populacao_selecionada[i:i+2] for i in range(0, len(populacao_selecionada), 2)]
        cromossomos_filhos = []
        for par in pares_de_cromossomos:
            pai = par[0]
            mae = par[1]
            filho_um = pai
            filho_dois = mae
            for disciplina_pai, disciplina_mae, disciplina_um, disciplina_dois in zip(pai.lista, mae.lista, filho_um.lista, filho_dois.lista):
                disciplina_um.sala = disciplina_mae.sala
                disciplina_dois.sala = disciplina_pai.sala
                disciplina_um.aptidao_sala = disciplina_um.aptidao_horario = 0
                disciplina_dois.aptidao_sala = disciplina_dois.aptidao_horario = 0 
            cromossomos_filhos += [filho_um, filho_dois]
        import pdb; pdb.set_trace()
        return cromossomos_filhos

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

for cromossomo in pop_inicial:
    cromossomo = AlgoritmoGenetico.aptidao(cromossomo)
    otimo, cromossomo = AlgoritmoGenetico.avaliacao(cromossomo)
    print(otimo)
cromossomos_melhores = AlgoritmoGenetico.selecao(pop_inicial)
cromossomos_filhos = AlgoritmoGenetico.cruzamento(cromossomos_melhores)

# solucionado, resultado = rodar_algoritmo_genetico(pop_inicial, ITERACOES_MAX)
# if solucionado: # Retorna um cromossomo
#     print('Cromossomo otimo:')
#     print(resultado)
# else: # Retorna uma populacao
#     print('Iteracoes maximas atingidas: ')
#     print(resultado)

# def rodar_algoritmo_genetico(populacao, iteracoes, contador=0):
#     def verificar_otimo(populacao):
#         for cromossomo in populacao:
#             cromossomo = aptidao(cromossomo)
#             otimo, cromossomo = avaliacao(cromossomo)
#             if otimo:
#                 return True, cromossomo
#         return False, cromossomo

#     if iteracoes == contador:
#         return False, populacao
#     achou_otimo, cromossomo = verificar_otimo(populacao)
#     if achou_otimo:
#         return True, cromossomo
#     populacao_selecionada = selecao(populacao)
#     cromossomos_filhos = cruzamento(populacao_selecionada)
#     filhos_adolescentes = mutacao(cromossomos_filhos)
#     achou_otimo_filho, cromossomo_filho = verificar_otimo(filhos_adolescentes)
#     if achou_otimo_filho:
#         return True, cromossomos_filho
#     nova_populacao = populacao_selecionada + filhos_adolescentes
#     rodar_tudo(nova_populacao, iteracoes, contador+1)

# solucionado, resultado = rodar_algoritmo_genetico(pop_inicial, ITERACOES_MAX)
# if solucionado: # Retorna um cromossomo
#     print('Cromossomo otimo:')
#     print(resultado)
# else: # Retorna uma populacao
#     print('Iteracoes maximas atingidas: ')
#     print(resultado)
