from Database.organizarDados import Dados
import gurobipy as gp

[materias, carga_horaria, professores, horarios] = Dados.organizarDados()

m = gp.Model()

"""Variáveis de Decisão"""
x = m.addVars(materias, professores, horarios, vtype=gp.GRB.BINARY)

"""Criação da Função Objetivo"""
m.setObjective(x.sum('*', '*', '*'), sense=gp.GRB.MINIMIZE)

""" Criação das Restrições """

"""Cada matéria tem uma carga horária"""
# c1 = m.addConstrs(x.sum('*', j, '*') == carga_horaria[j] for j in materias)
# "Em um determinado dia e horario, terá no máximo uma matéria"
# c2 = m.addConstrs(x.sum(i, '*', k) <= 1 for i in materias for k in horarios)
# "Em uma determinada matéria e horario, terá no máximo uma matéria"
# c3 = m.addConstrs(x.sum('*', j, k) <= 1 for j in materia for k in horario)

"""Executa o modelo"""
m.optimize()
#
# for i in professores:
#     for k in horarios:
#         for j in materias:
#             if x[i, j, k].X == 1:
#                 print(i, j, k, x[i, j, k].X)


