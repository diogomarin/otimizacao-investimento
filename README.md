
# Otimização de Investimentos

Este projeto implementa um **algoritmo genético** para otimizar a alocação de uma carteira de investimentos com base em dados fornecidos. A solução maximiza o retorno esperado ao respeitar os limites de capital disponível e riscos predefinidos para as carteiras de alto, médio e baixo risco.

O projeto utiliza uma abordagem orientada a objetos (POO) para gerenciar os dados de investimentos, definir a lógica da carteira e aplicar o algoritmo genético.


## Instalação

Para configurar o projeto localmente, siga as etapas abaixo:

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/otimizacao-investimentos.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd otimizacao-investimentos
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## Funcionalidades

Este projeto oferece as seguintes funcionalidades:

- **Algoritmo Genético para Otimização de Investimentos**:
  - Geração de carteiras de investimento com diferentes níveis de risco (Alto, Médio e Baixo).
  - Avaliação e seleção das carteiras mais promissoras com base no retorno esperado e no limite de capital disponível.
  - Operações de mutação e cruzamento para evoluir as soluções ao longo de várias gerações.

- **Estrutura de POO**:
  - `Investimento`: Representa cada investimento com atributos como custo, retorno e risco.
  - `Carteira`: Gerencia as opções de investimento e avalia soluções com base na função objetivo.
  - `AlgoritmoGenetico`: Implementa a lógica do algoritmo genético, incluindo geração de população, mutação, cruzamento e elitismo.

- **Teste Automatizado com pytest**:
  - Teste da função de avaliação (função objetivo) em diferentes cenários (ex.: capital zero, tetos zero, soluções válidas).

## Como Usar

### 1. Carregamento de Investimentos

O algoritmo utiliza um arquivo `investimentos.txt` como base de dados, que deve estar formatado da seguinte forma:

```
ID,Descrição,Custo,Retorno,Risco,
1,Projeto IA Avançada,300000,320000,Baixo,
2,Ferramenta de Big Data,200000,250000,Baixo,
...
```

Você pode personalizar os dados de investimentos conforme necessário.

### 2. Executando o Algoritmo Genético

Para executar o algoritmo genético e encontrar a melhor carteira de investimentos:

```python
from otimizacao_investimentos import Carteira, AlgoritmoGenetico

# Inicializando a carteira e carregando os investimentos
carteira = Carteira(capital_disponivel=3000000, teto_alto=300000, teto_medio=500000, teto_baixo=1000000)
carteira.carregar_investimentos('investimentos.txt')

# Executando o algoritmo genético
algoritmo_genetico = AlgoritmoGenetico(carteira)
melhor_carteira = algoritmo_genetico.executar()

# Exibindo a melhor carteira encontrada
print(melhor_carteira)
```

### 3. Executando Testes

Para rodar os testes com pytest, execute o seguinte comando no terminal:

```bash
pytest
```

Isso executará todos os testes definidos no projeto, validando o comportamento correto das funções.

## Melhorias Futuras

Algumas melhorias que podem ser implementadas no projeto incluem:

1. **Interface Gráfica (GUI)**:
   - Adicionar uma interface gráfica para permitir que os usuários escolham os investimentos manualmente e vejam os resultados do algoritmo genético em tempo real.

2. **Integração com APIs de Investimento**:
   - Conectar a aplicação a APIs externas para obter dados de mercado em tempo real, atualizando automaticamente as opções de investimento.

3. **Relatórios Detalhados**:
   - Gerar relatórios gráficos e em PDF mostrando a performance de diferentes soluções, incluindo o retorno total esperado, risco médio e capital investido.

4. **Aprimoramento da Heurística Genética**:
   - Ajustar os parâmetros do algoritmo genético, como mutação e cruzamento, com base em técnicas mais avançadas de otimização heurística.

5. **Simulações de Cenários Econômicos**:
   - Implementar uma simulação de diferentes cenários econômicos para testar a robustez das carteiras otimizadas, como crises financeiras ou mudanças de política monetária.

## Conclusão

Este projeto demonstra como um algoritmo genético pode ser aplicado para otimizar carteiras de investimento, respeitando as restrições de risco e capital. A modularidade e organização em POO tornam a solução fácil de manter e ampliar, enquanto o uso de `pytest` garante a confiabilidade das funcionalidades.

