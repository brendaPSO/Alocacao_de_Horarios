from Database.organizarDados import Dados
import gurobipy as gp

[prof_materia, horarios, carga, list_materia, list_prof] = Dados.organizarDados()

m = gp.Model()

"""Variáveis de Decisão"""
x = m.addVars(prof_materia, horarios, vtype=gp.GRB.BINARY)

"""Criação da Função Objetivo"""
m.setObjective(x.sum('*', '*'), sense=gp.GRB.MINIMIZE)

""" Criação das Restrições """

"""Cada prof_matéria tem uma carga horária"""
c1 = m.addConstrs(x.sum(value, '*') == carga[value] for i, value in enumerate(prof_materia))
"Em uma determinada materia e horario, terá no máximo um professor"
# c2 = m.addConstrs(x.sum('*', j) <= 1 for j in horarios)

"""Executa o modelo"""
m.optimize()

for i, value in enumerate(prof_materia):
    for k in horarios:
        if round(x[value, k].X) == 1:
            print(value, k, x[value, k].X)
