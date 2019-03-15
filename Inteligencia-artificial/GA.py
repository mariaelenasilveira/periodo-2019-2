from random import randint

#Setando os parâmetros
tamanhoPopulacao = 8
taxaMutacao = 0.01
taxaCruzamento = 0.98
numeroGeracoes = 3
minimo = -10
maximo = 10

#suponto um valor a ser encontrado, para ser usado como critério de parada
valorObjetivo = 27

#Gerando população inicial com individuos inteiros
def gerarPopulacaoInicial():
	x = [randint(minimo,maximo) for i in range(tamanhoPopulacao)]
	y = [randint(minimo,maximo) for i in range(tamanhoPopulacao)]
	return x, y

#Teste de Aptidao
def verificarAptidao():
	for i in range(tamanhoPopulacao):
		aptidoes.append(funcObjetivo(populacaoX[i],populacaoY[i]))
	return aptidoes

#Avaliando as aptidoes
def avaliarPopulacao():
	for i in range(tamanhoPopulacao):
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
	while i < tamanhoPopulacao:
		competidor1 = aptidoes[i] - valorObjetivo
		competidor2 = aptidoes[i+1] - valorObjetivo
		resultado = abs(competidor1) - abs(competidor2)
		if resultado < 0:
			ganhador = i
		else:
			ganhador = i+1
		selecionados.append(ganhador)
		i = i+2
	print("individuos selecionados",selecionados)



#Iteracoes
#Selecao
#Cruzamento
#Mutacao
#Elitismo
#Avaliacao

def funcObjetivo(x, y):
	aptidao = x ** 2 - 2*x*y + 6*x + y ** 2 - 6*y
	return aptidao


populacaoX, populacaoY = gerarPopulacaoInicial()
print("popX: ",populacaoX," popY: ", populacaoY)
aptidoes = []
print("respectivas aptidoes de cada cromossomo: ", verificarAptidao())

individuoOtimo = avaliarPopulacao()
if individuoOtimo != None:
	print("ponto otimo: ", populacaoX[individuoOtimo],populacaoY[individuoOtimo])
else:
	selecaoTorneio()