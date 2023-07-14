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
    
imprimir_solucao([6, 1, 2, 1, 2, 0, 2, 2, 0, 0])

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

funcao_custo([6, 1, 2, 1, 2, 0, 2, 2, 0, 0])
