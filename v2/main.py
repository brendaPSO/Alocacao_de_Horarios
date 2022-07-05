from Database.organizarDados import Dados
import gurobipy as gp

[prof_materia, horarios, carga_materia, materia, professor, dia, dia_horario] = Dados.organizarDados()

m = gp.Model()

"""Variáveis de Decisão"""
x = m.addVars(professor, materia, horarios, dia, vtype=gp.GRB.BINARY)

"""Criação da Função Objetivo"""
m.setObjective(x.sum('*', '*', '*', '*'), sense=gp.GRB.MINIMIZE)

""" Criação das Restrições """

"""Cada prof_matéria tem uma carga horária"""
c1 = m.addConstrs(x.sum(prof_materia[j].strip(), j, '*', '*') == carga_materia[j] for j in materia)

"Em uma determinada materia e horario, terá no máximo um professor"
c2 = m.addConstrs(x.sum('*', j, k, '*') <= 1 for j in materia for k in horarios)

"Em uma determinado professor e horario, terá no máximo uma matéria"
c2 = m.addConstrs(x.sum(i, '*', k, d) <= 1 for i in professor for k in horarios for d in dia)

"""Executa o modelo"""
m.optimize()

for i in professor:
    for j in materia:
        for k in horarios:
            for d in dia:
                if round(x[i, j, k, d].X) == 1:
                    print(i, j, k, d)
