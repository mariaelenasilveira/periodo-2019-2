from random import randint
from random import random


#Setando os parâmetros
tamanhoPopulacao = 8
taxaMutacao = 0.02
taxaCruzamento = 0.98
numeroGeracoes = 3
minimo = -10
maximo = 10

#suponto um valor a ser encontrado, para ser usado como critério de parada
valorObjetivo = 27

#declarando variaveis globais necessarias
novaPopX = []
novaPopY = []
filhosX = []
filhosY = []
aptidoes = []

#Gerando população inicial com individuos inteiros
def gerarPopulacaoInicial():
	x = [randint(minimo,maximo) for i in range(tamanhoPopulacao)]
	y = [randint(minimo,maximo) for i in range(tamanhoPopulacao)]
	print("Populacao inicial gerada: popX: ", x," popY: ", y)
	return x, y

#Teste de Aptidao
def verificarAptidao(x, y):
	for i in range(len(x)):
		aptidoes.append(funcObjetivo(x[i],y[i]))
	print("respectivas aptidoes de cada cromossomo: ", aptidoes)
	return aptidoes

#Avaliando as aptidoes
def avaliarPopulacao():
	for i in range(len(aptidoes)):
		if aptidoes[i] == valorObjetivo:
			return i #retorna a posicao do individuo otimo
	return None

#Selecao dos melhores: 
'''será feita selecao por torneio,em cada dois individuos será verificado
o quao proxima sua aptidao está do valor procurado. o que estiver mais proximo
será selecionado. assim ficará apenas com metade da população.
''' 
selecionados = []
ganhador = 0
def selecaoTorneio():
	i = 0 
	while i < len(aptidoes):
		competidor1 = aptidoes[i] - valorObjetivo
		competidor2 = aptidoes[i+1] - valorObjetivo
		resultado = abs(competidor1) - abs(competidor2)
		if resultado < 0:
			ganhador = i
		else:
			ganhador = i+1
		selecionados.append(ganhador)
		i = i+2
	print("individuos selecionados por torneio: ",selecionados)

#Cruzamento 
#O cruzamento irá manter a variavel x e trocar a variavel y dos pais
def cruzamento():
	for i in range(len(selecionados)):
		indice = selecionados[i]
		novaPopX.append(populacaoX[indice])
		novaPopY.append(populacaoY[indice])
	print("cruzamento selecionados: novaPopX: ", novaPopX, " novaPopY: ", novaPopY)
	i=0
	while i < len(selecionados):
		filhosX.append(novaPopX[i])
		filhosY.append(novaPopY[i+1])
		filhosX.append(novaPopX[i+1])
		filhosY.append(novaPopY[i])
		i = i+2
	print("filhos gerados: filhosX: ", filhosX, "filhosY: ", filhosY)

#Mutacao
''' se o valor aleatorio gerado, estiver dentro da faiza da taxa de mutacao
o valor de y do primeiro e segundo cromossomo incrementam 1'''
def mutacao():
	testeProbabilidade = random()
	if testeProbabilidade < taxaMutacao:
		filhosY[0] = filhosY[0] + 1
		filhosY[1] = filhosY[1] + 1

#nova populacao
''' junta os pais que foram selecionados no torneio e os filhos gerados'''
def novaPopulacao():
	populacaoX = []
	populacaoY = []
	for i in range(int(len(aptidoes))):
		populacaoX.append(novaPopX[i])
		populacaoY.append(novaPopY[i])
	for i in range(int(len(aptidoes))):
		populacaoX.append(filhosX[i])
		populacaoY.append(filhosY[i])
	print("Atual popX: ",populacaoX," Atual popY: ", populacaoY)

#Funcao objetivo
def funcObjetivo(x, y):
	aptidao = x ** 2 - 2*x*y + 6*x + y ** 2 - 6*y
	return aptidao


#Algoritmo:
print("Geracao 0")
populacaoX, populacaoY = gerarPopulacaoInicial()
verificarAptidao(populacaoX, populacaoY)
individuoOtimo = avaliarPopulacao()
iteracoes = 0
while iteracoes < numeroGeracoes:
	if individuoOtimo != None:
		print("ponto otimo encontrado: ", populacaoX[individuoOtimo],populacaoY[individuoOtimo])
		break
	else:
		selecaoTorneio()
		cruzamento()
		mutacao()
		del aptidoes[:]
		print("avaliando novos individuos")
		verificarAptidao(filhosX, filhosY)
		avaliarPopulacao()
		del selecionados[:]
		if individuoOtimo != None:
			print("ponto otimo encontrado: ", populacaoX[individuoOtimo],populacaoY[individuoOtimo])
			break
		print(" ")
		print("Inicio de uma nova geracao:", iteracoes+1)
		novaPopulacao()
		del aptidoes[:]
		verificarAptidao(populacaoX, populacaoY)
		del selecionados[:]
		iteracoes = iteracoes +1
		del novaPopX[:]
		del novaPopY[:]
		del filhosX[:]
		del filhosY[:]
