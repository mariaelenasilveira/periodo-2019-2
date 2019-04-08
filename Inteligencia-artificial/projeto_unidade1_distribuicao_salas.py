from random import random, uniform, randint, randrange, choice
import math
import csv

TURMAS_PEQUENAS = 25
TURMAS_GRANDES = 50
TURNO = {
    'M' : 1,
    'T' : 2,
    'N' : 3
}
QUANTITADE_DISCIPLINA = 20
TAMANHO_POPULACAO = 16
ITERACOES_MAX = 10
TAXA_MUTACAO = 0.03

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
        return cromossomos_filhos

    @staticmethod
    def mutacao(cromossomos):
        # modificar apenas as 3 primeiras disciplinas de 2 cromossomos terao sua sala modificada 
        teste_probabilidade = random()
        if teste_probabilidade < TAXA_MUTACAO:
            for cromossomo in cromossomos[:2]:
                for disciplina in cromossomo.lista[:3]:
                    disciplina.sala = randint(1,10)
        return cromossomos

        
lista = Disciplina.lista_de_disciplinas(QUANTITADE_DISCIPLINA)
cromossomos = Cromossomos(lista)
pop_inicial = cromossomos.populacao_inicial(TAMANHO_POPULACAO)


def rodar_algoritmo_genetico(populacao, iteracoes, contador=0):
    def verificar_otimo(populacao):
        for cromossomo in populacao:
            cromossomo = AlgoritmoGenetico.aptidao(cromossomo)
            otimo, cromossomo = AlgoritmoGenetico.avaliacao(cromossomo)
            if otimo:
                return True, cromossomo
        return False, cromossomo

    if iteracoes == contador:
        return False, populacao
    achou_otimo, cromossomo = verificar_otimo(populacao)
    if achou_otimo:
        return True, cromossomo
    populacao_selecionada = AlgoritmoGenetico.selecao(populacao)
    cromossomos_filhos = AlgoritmoGenetico.cruzamento(populacao_selecionada)
    cromossomos_filhos_mutados = AlgoritmoGenetico.mutacao(cromossomos_filhos)
    achou_otimo_filho, cromossomo_filho = verificar_otimo(cromossomos_filhos_mutados)
    if achou_otimo_filho:
        return True, cromossomos_filho
    nova_populacao = populacao_selecionada + cromossomos_filhos_mutados
    # import pdb; pdb.set_trace()
    return rodar_algoritmo_genetico(nova_populacao, iteracoes, contador+1)

# Ao terminar a quantidade de iteracoes será retornado a população da ultima iteração. 
# Avalia o melhor cromossomo da última população.
def avaliacao_final(populacao):
    def torneio(cromossomo):
        soma = 0
        for disciplina in cromossomo.lista:
            soma += disciplina.aptidao_horario*disciplina.aptidao_sala
        return soma

    melhor_cromossomo_final = max(populacao, key=torneio)
    return melhor_cromossomo_final

solucionado, resultado = rodar_algoritmo_genetico(pop_inicial, ITERACOES_MAX)
melhor_cromossomo_final = avaliacao_final(resultado)
horario_aula = []
turno_aula = []
if solucionado: # Retorna um cromossomo
    print('Cromossomo otimo:')
    # print(resultado)
    melhor_cromossomo_final = resultado
else: # Retorna uma populacao
    melhor_cromossomo_final = avaliacao_final(resultado)
    print('QUANTIDADE DE ITERAÇÕES MÁXIMA ATINGIDA! ')
    for disciplina in melhor_cromossomo_final.lista:
    	switcher = {
    		1: "M12",
    		2: "M34",
    		3: "M56",
    		4: "T12",
    		5: "T34",
    		6: "T56",
    		7: "N12",
    		8: "N34",
    	}
    	horario_aula.append(switcher.get(disciplina.horario, "nothing"))
    	switcher = {
    		1: "Manhã",
    		2: "Tarde",
    		3: "Noite",    		
    	}
    	turno_aula.append(switcher.get(disciplina.turno, "nothing"))

print("*"*50)
print("Resultado final para distribuição das salas: ")    	
file = open('tabela.csv', 'w')
try:
    writer = csv.writer(file)
    writer.writerow(("ID_DISCIPLINA", "TAMANHO DA TURMA", "TURNO", "HORÁRIO DE AULA", "SALA"))
    for disciplina, horario_aula_n, turno_aula_n in zip(melhor_cromossomo_final.lista, horario_aula, turno_aula):
        writer.writerow((disciplina.id_disciplina, disciplina.tamanho, turno_aula_n, horario_aula_n, disciplina.sala))
finally:
    file.close()

print(open('tabela.csv', 'rt').read())
