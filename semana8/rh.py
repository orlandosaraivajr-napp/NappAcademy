from rh.classes.Departamento import Departamento

from datetime import date, timedelta
dt1 = date.today() - timedelta(days=4)
hoje = date.today()

departamento = Departamento('Departamento XYZ')
departamento.informar_responsavel('José da Silva', dt1.day, dt1.month, 1990)
departamento.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
departamento.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
departamento.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
departamento.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1985)

aniversariantes = departamento.verificar_aniversariantes()

for aniversariante in aniversariantes:
    print('Parabéns ' + aniversariante[0] + ' pelo seu dia')
