import random

class Investimento:
    def __init__(self, opcao, descricao, custo, retorno, risco):
        self.opcao = int(opcao)
        self.descricao = descricao
        self.custo = int(custo)
        self.retorno = int(retorno)
        self.risco = risco
        self.atratividade = round(self.retorno / self.custo, 2)


class Carteira:
    def __init__(self, capital_disponivel, teto_alto, teto_medio, teto_baixo):
        self.capital_disponivel = capital_disponivel
        self.teto_alto = teto_alto
        self.teto_medio = teto_medio
        self.teto_baixo = teto_baixo
        self.opcoes_investimento = []
        self.pesos = {}

    def carregar_investimentos(self, arquivo):
        for linha in open(arquivo):
            opcao, descricao, custo, retorno, risco, _ = linha.split(',')
            investimento = Investimento(opcao, descricao, custo, retorno, risco)
            self.opcoes_investimento.append(investimento)
            self.pesos[investimento.opcao] = investimento.atratividade

    def dominio(self):
        return [invest.opcao for invest in self.opcoes_investimento]

    def funcao_objetivo(self, solucao):
        capital_investido = 0
        retorno_a = retorno_m = retorno_b = 0
        carteira_a = []
        carteira_m = []
        carteira_b = []
        
        for i in solucao:
            if i <= len(self.opcoes_investimento):  # Verifica se o índice está dentro do intervalo válido
                investimento = self.opcoes_investimento[i - 1]  # Ajuste para 0-based
            else:
                continue  # Se o índice estiver fora do intervalo, ignore

            if investimento.risco == 'Alto' and retorno_a + investimento.retorno <= self.teto_alto and capital_investido + investimento.custo <= self.capital_disponivel:
                retorno_a += investimento.retorno
                capital_investido += investimento.custo
                carteira_a.append(investimento.descricao)
            elif investimento.risco == 'Medio' and retorno_m + investimento.retorno <= self.teto_medio and capital_investido + investimento.custo <= self.capital_disponivel:
                retorno_m += investimento.retorno
                capital_investido += investimento.custo
                carteira_m.append(investimento.descricao)
            elif investimento.risco == 'Baixo' and retorno_b + investimento.retorno <= self.teto_baixo and capital_investido + investimento.custo <= self.capital_disponivel:
                retorno_b += investimento.retorno
                capital_investido += investimento.custo
                carteira_b.append(investimento.descricao)
        
        retorno_final = retorno_a + retorno_m + retorno_b
        retorno_por_risco = [retorno_a, retorno_m, retorno_b]
        carteira_por_risco = [carteira_a, carteira_m, carteira_b]

        return [retorno_final, capital_investido, retorno_por_risco, carteira_por_risco]


class AlgoritmoGenetico:
    def __init__(self, carteira, tamanho_populacao=100, p=0.9, prob_mutacao=0.2, elitismo=0.2, num_geracoes=100):
        self.carteira = carteira
        self.tamanho_populacao = tamanho_populacao
        self.p = p
        self.prob_mutacao = prob_mutacao
        self.elitismo = elitismo
        self.num_geracoes = num_geracoes

    def gerar_populacao_inicial(self):
        return [random.sample(self.carteira.dominio(), len(self.carteira.dominio())) for _ in range(self.tamanho_populacao)]

    def mutacao(self, solucao):
        i = random.randint(0, len(solucao) - 1)
        if random.random() < self.p:
            if self.carteira.pesos[solucao[i]] < self.p:
                return random.sample(solucao, len(solucao))
            return solucao
        return random.sample(solucao, len(solucao))

    def cruzamento(self, solucao1, solucao2):
        i = random.randint(1, len(solucao1) - 1)
        return list(dict.fromkeys(solucao1[:i] + solucao2[i:]))

    def executar(self):
        populacao = self.gerar_populacao_inicial()
        numero_elitismo = int(self.elitismo * self.tamanho_populacao)

        for _ in range(self.num_geracoes):
            carteiras_avaliadas = [(self.carteira.funcao_objetivo(individuo), individuo) for individuo in populacao]
            carteiras_avaliadas.sort(reverse=True)
            populacao = [individuo for (_, individuo) in carteiras_avaliadas[:numero_elitismo]]

            while len(populacao) < self.tamanho_populacao:
                if random.random() < self.prob_mutacao:
                    mutante = random.randint(0, numero_elitismo - 1)
                    populacao.append(self.mutacao(populacao[mutante]))
                else:
                    c1, c2 = random.sample(range(numero_elitismo), 2)
                    populacao.append(self.cruzamento(populacao[c1], populacao[c2]))

        return carteiras_avaliadas[0]


# Configuração de carteiras e limites
carteira = Carteira(capital_disponivel=3000000, teto_alto=300000, teto_medio=500000, teto_baixo=1000000)
carteira.carregar_investimentos('investimentos.txt')

# Execução do algoritmo genético
algoritmo_genetico = AlgoritmoGenetico(carteira)
melhor_carteira = algoritmo_genetico.executar()

# Exibindo os resultados
print('Melhor carteira para investimento é composta por:')
print('Opções de Alto Risco:', melhor_carteira[0][3][0])
print('Retorno Esperado para as Opções de Alto Risco:', melhor_carteira[0][2][0])
print('Opções de Médio Risco:', melhor_carteira[0][3][1])
print('Retorno Esperado para as Opções de Médio Risco:', melhor_carteira[0][2][1])
print('Opções de Baixo Risco:', melhor_carteira[0][3][2])
print('Retorno Esperado para as Opções de Baixo Risco:', melhor_carteira[0][2][2])
print('Capital Investido:', melhor_carteira[0][1])
print('Retorno Esperado Total:', melhor_carteira[0][0])
