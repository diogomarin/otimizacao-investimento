import random

opcoes_investimento = []
for linha in open('D:/GitHub/pratica-code/bootcamp-seletivo-enacom/investimentos.txt'):
    _opcao, _descricao, _custo, _retorno, _risco, _outro = linha.split(',')
    opcoes_investimento.append((_opcao, _descricao, int(_custo), int(_retorno), _risco))


dominio = []
for i in range(len(opcoes_investimento)):
    dominio.append(int(opcoes_investimento[i][0]) - 1)


def funcao_objetivo(solucao):
    capital_disponivel = 2700000
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

    return ('Cappital Investido:', capital_investido,
            'Retorno Esperado:', retorno_esperado,
            'Retorno Risco Alto:', retorno_a,
            'Retorno Risco Médio:', retorno_m,
            'Retorno Risco Baixo:',  retorno_b)

#funcao_objetivo(dominio)


def dominio_aleatorio():
    novo_dominio = []
    while len(novo_dominio) != len(dominio):
        d = random.randint(0, (len(dominio) - 1))
        if d not in novo_dominio:
            novo_dominio.append(d)

    return novo_dominio

# funcao_objetivo(dominio_aleatorio())