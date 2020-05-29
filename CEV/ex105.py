def notas(*num, sit=False):
    """
    -> Fução para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com varias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num)/len(num)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOM'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)


# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
# -Quantidade de notas
# -A maior nota
# -A menor nota
# -A média da turma
# -A situação(opcional)
# Adicione tambem as docstrings da função.
