
investimentos = {}
for linha in open('D:/GitHub/pratica-code/bootcamp-seletivo-enacom/investimentos.txt'):
    _opcao, _descricao, _custo, _retorno, _risco, _outro = linha.split(',')
    investimentos.setdefault((_opcao, _risco), [])
    investimentos[(_opcao, _risco)].append((_custo, _retorno))