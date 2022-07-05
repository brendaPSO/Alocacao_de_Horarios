# Criar professor

import gurobipy as gp

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
