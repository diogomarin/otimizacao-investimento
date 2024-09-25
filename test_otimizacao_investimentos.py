from otimizacao_investimentos import Carteira, Investimento, AlgoritmoGenetico

# Inicializando os parâmetros para o teste
capital_disponivel = 3000000
teto_carteira_a = 300000
teto_carteira_m = 500000
teto_carteira_b = 1000000

# Criar uma instância da classe Carteira
carteira = Carteira(capital_disponivel, teto_carteira_a, teto_carteira_m, teto_carteira_b)

# Função de teste para `funcao_objetivo`
def test_funcao_objetivo():
    # Carregar um arquivo de teste com investimentos
    carteira.carregar_investimentos('investimentos.txt')

    # Cenário 1: Caso de teste quando capital disponível é zero
    carteira_zero = Carteira(0, teto_carteira_a, teto_carteira_m, teto_carteira_b)
    dominio_aleatorio = [1, 2, 3]  # Simulação de um domínio aleatório para o teste
    resultado_zero = carteira_zero.funcao_objetivo(dominio_aleatorio)
    
    assert resultado_zero == [0, 0, [0, 0, 0], [[], [], []]], "Erro: Resultado esperado quando capital é zero."

    # Cenário 2: Caso de teste quando todos os tetos são zero
    carteira_sem_teto = Carteira(capital_disponivel, 0, 0, 0)
    resultado_sem_teto = carteira_sem_teto.funcao_objetivo(dominio_aleatorio)
    
    assert resultado_sem_teto == [0, 0, [0, 0, 0], [[], [], []]], "Erro: Resultado esperado quando os tetos são zero."

    # Cenário 3: Teste com um domínio válido e capital disponível
    dominio_valido = [1, 2, 3]  # Exemplo de uma solução possível
    resultado_valido = carteira.funcao_objetivo(dominio_valido)
    
    assert isinstance(resultado_valido[0], int), "Erro: O retorno final deve ser um inteiro."
    assert resultado_valido[1] <= capital_disponivel, "Erro: O capital investido excede o capital disponível."
    assert all(isinstance(x, list) for x in resultado_valido[3]), "Erro: As carteiras por risco devem ser listas."
    
    print("Todos os testes de `funcao_objetivo` passaram com sucesso.")

# Rodar o teste
test_funcao_objetivo()
