import random

opcoes_investimento = {}
pesos = {}

for linha in open('investimentos.txt'):
    _opcao, _descricao, _custo, _retorno, _risco, _outro = linha.split(',')
    
    opcoes_investimento.setdefault((int(_opcao)), [])
    opcoes_investimento[(int(_opcao))].append((int(_opcao), _descricao, int(_custo), int(_retorno), _risco))
    
    pesos.setdefault((int(_opcao)), [])
    pesos[(int(_opcao))].append((round(int(_retorno) / int(_custo),2)))
    
dominio = []
for i in range(1, len(opcoes_investimento) + 1):
    dominio.append((opcoes_investimento[i][0][0]))

capital_disponivel = 2400000
teto_carteira_a = 900000 #carteira de alto risco
teto_carteira_m = 1500000 #carteira de medio risco
teto_carteira_b = 1200000 #carteira de baixo risco

def funcao_objetivo(solucao):
    capital_investido = 0
    retorno_a = 0
    retorno_m = 0
    retorno_b = 0
    carteira_a = []
    carteira_m = []
    carteira_b = []
    atual = opcoes_investimento

    for i in range(1, len(solucao)):
        if (atual[solucao[i]][0][4] == 'Alto') and (retorno_a + atual[solucao[i]][0][3] <= teto_carteira_a) and (capital_investido + atual[solucao[i]][0][2] <= capital_disponivel):
            retorno_a += atual[solucao[i]][0][3]
            capital_investido += atual[solucao[i]][0][2]
            carteira_a.append((atual[solucao[i]][0][0], atual[solucao[i]][0][1]))
        elif (atual[solucao[i]][0][4] == 'Medio') and (retorno_m + atual[solucao[i]][0][3] <= teto_carteira_m) and (capital_investido + atual[solucao[i]][0][2] <= capital_disponivel):
            retorno_m += atual[solucao[i]][0][3]
            capital_investido += atual[solucao[i]][0][2]
            carteira_m.append((atual[solucao[i]][0][0], atual[solucao[i]][0][1]))
        elif (atual[solucao[i]][0][4] == 'Baixo') and (retorno_b + atual[solucao[i]][0][3] <= teto_carteira_b) and (capital_investido + atual[solucao[i]][0][2] <= capital_disponivel):
            retorno_b += atual[solucao[i]][0][3]
            capital_investido += atual[solucao[i]][0][2]
            carteira_b.append((atual[solucao[i]][0][0], atual[solucao[i]][0][1]))
            
        retorno_por_risco = [retorno_a, retorno_m, retorno_b]
        carteira_por_risco = [carteira_a, carteira_m, carteira_b]
        retorno_final = retorno_a + retorno_m + retorno_b
        
        resultado = [retorno_final, capital_investido, retorno_por_risco, carteira_por_risco]    

    return resultado

def dominio_aleatorio():
    novo_dominio = []
    while len(novo_dominio) != len(dominio):
        d = random.randint(1, (len(dominio)))
        if d not in novo_dominio:
            novo_dominio.append(d)

    return novo_dominio

def mutacao(dominio, p, solucao):    
    i = random.randint(0, (len(dominio) - 1))
    mutante = []
    
    if random.random() >= 0.5:
        if pesos[solucao[i]][0] < p:
            mutante = random.sample(solucao, len(solucao))
        if pesos[solucao[i]][0] >= p:
            mutante.append(solucao[i])
            while len(mutante) != len(dominio):
                d = random.randint(1, (len(dominio)))
                if d not in mutante:
                    mutante.append(d)
    else:
        mutante = random.sample(solucao, len(solucao))

    return mutante

def cruzamento(dominio, solucao1, solucao2):
    i = random.randint(0, (len(dominio) - 1))
    dict_aux = dict.fromkeys(solucao1[0:i] + solucao2[i:])
    unicos = list(dict_aux)
    falta = list(set(dominio) - set(unicos))
    cross = unicos + falta
    
    return cross    

def genetico(dominio_aleatorio, funcao_objetivo, tamanho_populacao = 100, p = 0.9, probabilidade_mutacao = 0.2, elitismo = 0.2, numero_geracoes = 100):   
    populacao = []
    carteiras_verificadas = []
    
    for i in range(tamanho_populacao):
        dominio = dominio_aleatorio()
        populacao.append(dominio)
        
    numero_elitismo = int(elitismo * tamanho_populacao)
    
    for i in range(numero_geracoes):
        carteiras = [(funcao_objetivo(individuo), individuo) for individuo in populacao]
        for i in range(len(carteiras) - 1):
            if len(carteiras[i][0][3][0]) >= 1 and len(carteiras[i][0][3][1]) >= 2 and len(carteiras[i][0][3][2]) >= 2:
                carteiras_verificadas.append(carteiras[i])
        
        carteiras_verificadas.sort()
        individuos_ordenados = [individuo for (retorno, individuo) in carteiras_verificadas]
        
        populacao = individuos_ordenados[0:numero_elitismo]
        
        while len(populacao) < tamanho_populacao:
            if random.random() < probabilidade_mutacao:
                m = random.randint(0, numero_elitismo)
                populacao.append(mutacao(dominio, p, individuos_ordenados[m]))
            else:
                c1 = random.randint(0, numero_elitismo)
                c2 = random.randint(0, numero_elitismo)
                populacao.append(cruzamento(dominio, individuos_ordenados[c1], individuos_ordenados[c2]))
    
    carteiras_verificadas.sort(reverse=True)
    
    return carteiras_verificadas[0]

solucao_genetico = genetico(dominio_aleatorio, funcao_objetivo)

print('Melhor carteira para investimento é composta por:')
print('- - - - - - - - - - - - - - - - - - - - - - - - -')
print('Opcoes de Alto Risco:', solucao_genetico[0][3][0])
print('Retorno Esperado para as Opcoes de Alto Risco:', solucao_genetico[0][2][0])
print('- - - - - - - - - - - - - - - - - - - - - - - - -')
print('Opcoes de Medio:', solucao_genetico[0][3][1])
print('Retorno Esperado para as Opcoes de Medio Risco:', solucao_genetico[0][2][1])
print('- - - - - - - - - - - - - - - - - - - - - - - - -')
print('Opcoes de Baixo Risco:', solucao_genetico[0][3][2])
print('Retorno Esperado para as Opcoes de Baixo Risco:', solucao_genetico[0][2][2])
print('- - - - - - - - - - - - - - - - - - - - - - - - -')
print('Capital Investido:', solucao_genetico[0][1])
print('Retorno Esperado:', solucao_genetico[0][0])
print('Atratividade:', round((solucao_genetico[0][0] / solucao_genetico[0][1]),2))