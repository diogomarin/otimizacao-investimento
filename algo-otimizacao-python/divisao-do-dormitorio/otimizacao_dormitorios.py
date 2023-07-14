
import math
import random

dormitorios = ['Sao Paulo', 'Flamengo', 'Coritiba', 'Cruzeiro', 'Fortaleza']

preferenciais = [('Amanda', ('Cruzeiro', 'Coritiba')),
                 ('Pedro', ('Sao Paulo', 'Fortaleza')),
                 ('Marcos', ('Flamengo', 'Sao Paulo')),
                 ('Priscila', ('Sao Paulo', 'Fortaleza')),
                 ('Jessica', ('Flamengo', 'Cruzeiro')),
                 ('Paulo', ('Coritiba', 'Fortaleza')),
                 ('Fred', ('Fortaleza', 'Flamengo')),
                 ('Suzana', ('Cruzeiro', 'Coritiba')),
                 ('Laura', ('Cruzeiro', 'Coritiba')),
                 ('Ricardo', ('Coritiba', 'Flamengo'))]

#restricoes (minimos e maximos)
dominio = [(0, (len(dormitorios)*2) - i - 1) for i in range(0, len(dormitorios) * 2)]

def imprimir_solucao(solucao):
    vagas = []
    for i in range(len(dormitorios)):
        vagas += [i, i]
    for i in range(len(solucao)):
        atual = solucao[i]
        dormitorio = dormitorios[vagas[atual]]
        print(preferenciais[i][0], dormitorio)
        del vagas[atual]
    
#imprimir_solucao([6, 1, 2, 1, 2, 0, 2, 2, 0, 0])

#penalidades - parte principal de um algoritmo de otimizacao (variaveis)
#colocar o aluno em um quarto que nao foi de sua preferencia
#colocar o aluno em nenhum quarto de suas preferencias
def funcao_custo(solucao):
    custo = 0
    vagas = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
    for i in range(len(solucao)):
        atual = solucao[i]
        dormitorio = dormitorios[vagas[atual]]
        preferencia = preferenciais[i][1]
        if preferencia[0] == dormitorio:
            custo += 0
        elif preferencia[1] == dormitorio:
            custo += 1
        else:
            custo += 3
        
        del vagas[atual]
    
    return custo

#funcao_custo([6, 1, 2, 1, 2, 0, 2, 2, 0, 0])

#implementacao da pesquisa randomica
def pesquisa_randomica(dominio, funcao_custo):
    melhor_custo = 999999999
    for i in range(0, 10000):
        solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
        custo = funcao_custo(solucao)
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_solucao = solucao
    return melhor_solucao

solucao_randomica = pesquisa_randomica(dominio, funcao_custo)
custo_randomica = funcao_custo(solucao_randomica)
print('------------------------')
print('SOLUCAO APENAS ALEATORIA')
print('------------------------')
imprimir_solucao(solucao_randomica)

def subida_encosta(dominio, funcao_custo):
    solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
    while True:
        vizinhos = []

        for i in range(len(dominio)):
            if solucao[i] > dominio[i][0]:
                 if solucao [i] != dominio[i][1]:
                     vizinhos.append(solucao[0:i] + [solucao[i] + 1] + solucao[i + 1:])
            if solucao [i] < dominio[i][1]:
                if solucao[i] != dominio[i][0]:
                  vizinhos.append(solucao[0:i] + [solucao[i] - 1] + solucao [i + 1:])
        atual = funcao_custo(solucao)
        melhor = atual
        for i in range(len(vizinhos)):
            custo = funcao_custo(vizinhos[i])
            if custo < melhor:
                melhor = custo
                solucao = vizinhos[i]
        
        if melhor == atual:
            break
    return solucao

solucao_subida_encosta = subida_encosta(dominio, funcao_custo)
custo_subida_encosta = funcao_custo(solucao_subida_encosta)
print('------------------------')
print('SOLUCAO HILL CLIMB')
print('------------------------')
imprimir_solucao(solucao_subida_encosta)

def tempera_simulada(dominio, funcao_custo, temperatura = 10000, resfriamento = 0.95, passo = 1):
    solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
    
    while temperatura > 0.1:
        i = random.randint(0, len(dominio) - 1)
        direcao = random.randint(-passo, passo)
        
        solucao_temp = solucao[:]
        solucao_temp[i] += direcao
        if solucao_temp[i] < dominio[i][0]:
            solucao_temp[i] = dominio[i][0]
        elif solucao_temp[i] > dominio[i][1]:
            solucao_temp[i] = dominio[i][1]
        
        custo_solucao = funcao_custo(solucao)
        custo_solucao_temp = funcao_custo(solucao_temp)
        probabilidade = pow(math.e, (-custo_solucao_temp - custo_solucao) / temperatura)
        
        if (custo_solucao_temp < custo_solucao or random.random() < probabilidade):
            solucao = solucao_temp
            
        temperatura = temperatura * resfriamento
        
    return solucao

solucao_tempera_simulada = tempera_simulada(dominio, funcao_custo)
custo_tempera_simulada = funcao_custo(solucao_tempera_simulada)
print('------------------------')
print('SOLUCAO TEMPERA SIMULADA')
print('------------------------')
imprimir_solucao(solucao_tempera_simulada)

def mutacao(dominio, passo, solucao):
    i = random.randint(0, len(dominio) - 1)
    mutante = solucao
    
    if random.random() < 0.5:
        if solucao[i] != dominio[i][0]:
            mutante = solucao[0:i] + [solucao[i] - passo] + solucao[i + 1:]
    else:
        if solucao[i] != dominio[i][1]:
            mutante = solucao[0:i] + [solucao[i] + passo] + solucao[i + 1:]
    
    return mutante

#s = [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]
#s1 = mutacao(dominio, 1, s)

def cruzamento(dominio, solucao1, solucao2):
    i = random.randint(1, len(dominio)- 2)
    return solucao1[0:i] + solucao2[i:]

#s1 = [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]
#s2 = [0, 1, 2, 5, 8, 9, 2, 3, 5, 1, 0, 6]
#s3 = cruzamento(dominio, s1, s2)

def genetico(dominio, funcao_custo, tamanho_populacao = 50, passo = 1, probabilidade_mutacao = 0.2, elitismo = 0.2, numero_geracoes = 100):
    populacao = []
    for i in range(tamanho_populacao):
        solucao = [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]
        populacao.append(solucao)
        
    numero_elitismo = int(elitismo * tamanho_populacao)
    
    for i in range(numero_geracoes):
        custos = [(funcao_custo(individuo), individuo) for individuo in populacao]
        custos.sort()
        individuos_ordenados = [individuo for (custo, individuo) in custos]
        
        populacao = individuos_ordenados[0:numero_elitismo]
        
        while len(populacao) < tamanho_populacao:
            if random.random() < probabilidade_mutacao:
                m = random.randint(0, numero_elitismo)
                populacao.append(mutacao(dominio, passo, individuos_ordenados[m]))
            else:
                c1 = random.randint(0, numero_elitismo)
                c2 = random.randint(0, numero_elitismo)
                populacao.append(cruzamento(dominio, individuos_ordenados[c1], individuos_ordenados[c2]))
    
    return custos[0][1]

solucao_genetico = genetico(dominio, funcao_custo)
custo_genetico = funcao_custo(solucao_genetico)
print('------------------------')
print('SOLUCAO GENETICA')
print('------------------------')
imprimir_solucao(solucao_genetico)