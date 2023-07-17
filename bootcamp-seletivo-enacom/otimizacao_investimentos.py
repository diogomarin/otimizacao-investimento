import random

opcoes_investimento = []
for linha in open('D:/GitHub/pratica-code/bootcamp-seletivo-enacom/investimentos.txt'):
    _opcao, _descricao, _custo, _retorno, _risco, _outro = linha.split(',')
    opcoes_investimento.append((_opcao, _descricao, int(_custo), int(_retorno), _risco))


dominio = []
for i in range(len(opcoes_investimento)):
    dominio.append(int(opcoes_investimento[i][0]) - 1)


def funcao_objeto(solucao):
    capital_disponivel = 2400000
    capital_investido = 0
    retorno_a = 0
    retorno_m = 0
    retorno_b = 0
    carteira = []
    atual = opcoes_investimento
    
    for i in range(len(solucao)):
        if (atual[solucao[i]][4] == 'Alto') and (retorno_a + atual[solucao[i]][3] <= 900000) and (capital_investido + atual[solucao[i]][2] <= capital_disponivel):
            retorno_a += atual[solucao[i]][3]
            capital_investido += atual[solucao[i]][2]
            carteira.append((atual[solucao[i]][0], atual[solucao[i]][1]))
        elif (atual[solucao[i]][4] == 'Médio') and (retorno_m + atual[solucao[i]][3] <= 1500000) and (capital_investido + atual[solucao[i]][2] <= capital_disponivel):
            retorno_m += atual[solucao[i]][3]
            capital_investido += atual[solucao[i]][2]
            carteira.append((atual[solucao[i]][0], atual[solucao[i]][1]))
        elif (atual[solucao[i]][4] == 'Baixo') and (retorno_b + atual[solucao[i]][3] <= 1200000) and (capital_investido + atual[solucao[i]][2] <= capital_disponivel):
            retorno_b += atual[solucao[i]][3]
            capital_investido += atual[solucao[i]][2]
            carteira.append((atual[solucao[i]][0], atual[solucao[i]][1]))
            
        retorno_esperado = retorno_a + retorno_m + retorno_b

    # return ('Cappital Investido:', capital_investido,
    #         'Retorno Esperado:', retorno_esperado,
    #         'Retorno Risco Alto:', retorno_a,
    #         'Retorno Risco Médio:', retorno_m,
    #         'Retorno Risco Baixo:',  retorno_b)
    
    return retorno_esperado

#funcao_objeto(dominio)


def dominio_aleatorio():
    novo_dominio = []
    while len(novo_dominio) != len(dominio):
        d = random.randint(0, (len(dominio) - 1))
        if d not in novo_dominio:
            novo_dominio.append(d)

    return novo_dominio

#funcao_objeto(dominio_aleatorio())


def mutacao(dominio, passo, solucao):
    i = random.randint(0, (len(dominio) - 1))
    mutante = solucao
    
    if random.random() < 0.5:
        if solucao[i] != dominio[i] and solucao[i] != 0:
            mutante = solucao[0:i] + [solucao[i] - passo] + solucao[i + 1:]
    else:
        if solucao[i] != dominio[i] and solucao[i] != 12:
            mutante = solucao[0:i] + [solucao[i] + passo] + solucao[i + 1:]
    
    return mutante

# s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# mutacao(dominio, 1, s)

def cruzamento(dominio, solucao1, solucao2):
    i = random.randint(0, (len(dominio) - 1))
    return solucao1[0:i] + solucao2[i:]

# s1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# s2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# cruzamento(dominio, s1, s2)

def genetico(dominio_aleatorio, funcao_objeto, tamanho_populacao = 10, passo = 1, probabilidade_mutacao = 0.2, elitismo = 0.2, numero_geracoes = 100):
    populacao = []
    for i in range(tamanho_populacao):
        solucao = dominio_aleatorio()
        populacao.append(solucao)
        
    numero_elitismo = int(elitismo * tamanho_populacao)
    
    for i in range(numero_geracoes):
        valores = [(funcao_objeto(individuo), individuo) for individuo in populacao]
        valores.sort()
        individuos_ordenados = [individuo for (valor, individuo) in valores]
        
        populacao = individuos_ordenados[0:numero_elitismo]
        
        while len(populacao) < tamanho_populacao:
            if random.random() < probabilidade_mutacao:
                m = random.randint(0, numero_elitismo)
                populacao.append(mutacao(solucao, passo, individuos_ordenados[m]))
            else:
                c1 = random.randint(0, numero_elitismo)
                c2 = random.randint(0, numero_elitismo)
                populacao.append(cruzamento(solucao, individuos_ordenados[c1], individuos_ordenados[c2]))
    
    return valores[0]

#solucao_genetico = genetico(dominio_aleatorio, funcao_objeto)
