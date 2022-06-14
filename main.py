# Criar professor

import gurobipy as gp
import pandas as pd

df = pd.read_csv('./dados.csv', sep=',')

vet_dias = list(df.values.base[0])
vet_materias = list(df.values.base[1])
vet_horarios = list(df.values.base[2])
vet_carga = list(df.values.base[3])

rotulo_m = ["{}".format(valor) for idx, valor in enumerate(vet_materias)]
dia = ["{}".format(valor) for idx, valor in enumerate(vet_dias)]
horario = ["{}".format(valor) for idx, valor in enumerate(vet_horarios)]

materia = dict()
for idx, valor in enumerate(rotulo_m):
    materia[valor] = 1

carga_horaria = dict()
for j, key in enumerate(rotulo_m):
    carga_horaria[key] = vet_carga[j]

m = gp.Model()

"""Variáveis de Decisão"""
x = m.addVars(dia, materia, horario, vtype=gp.GRB.BINARY)

"""Criação da Função Objetivo"""
m.setObjective(x.sum('*', '*', '*'), sense=gp.GRB.MINIMIZE)

""" Criação das Restrições """

"""Cada matéria tem uma carga horária"""
c1 = m.addConstrs(x.sum('*', j, '*') == carga_horaria[j] for j in materia)
"Em um determinado dia e horario, terá no máximo uma matéria"
c2 = m.addConstrs(x.sum(i, '*', k) <= 1 for i in dia for k in horario)
"Em uma determinada matéria e horario, terá no máximo uma matéria"
# c3 = m.addConstrs(x.sum('*', j, k) <= 1 for j in materia for k in horario)

"""Executa o modelo"""
m.optimize()

for i in dia:
    for k in horario:
        for j in materia:
            if x[i, j, k].X == 1:
                print(i, j, k, x[i, j, k].X)
