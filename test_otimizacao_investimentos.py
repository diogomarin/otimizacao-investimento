from otimizacao_investimentos import *

def test_funcao_objetivo():
    if capital_disponivel == 0:
        assert funcao_objetivo(dominio_aleatorio) == [0, 0, [0, 0, 0], [[], [], []]]
    if teto_carteira_a == 0 and teto_carteira_m == 0 and teto_carteira_b == 0:
        assert funcao_objetivo(dominio_aleatorio) == [0, 0, [0, 0, 0], [[], [], []]]