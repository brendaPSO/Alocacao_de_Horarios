from Database.organizarDados import Dados
import gurobipy as gp

[prof_materia, horarios, carga_materia, materias, professores, dias] = Dados.organizarDados()

model = gp.Model()

# ====== Variáveis de Decisão
x = model.addVars(professores, materias, horarios, dias, vtype=gp.GRB.BINARY)


# ====== Criação da Função Objetivo
model.setObjective(gp.quicksum(x[p, m, h, d] for p in professores for m in materias for h in horarios for d in dias),
                   sense=gp.GRB.MINIMIZE)


# ====== Criação das Restrições

"""Cada matéria do professor tem uma carga horária"""
c1 = model.addConstrs(x.sum(prof_materia[m].strip(), m, '*', '*') == carga_materia[m] for m in materias)

"Em uma determinada materia, horario e dia, terá no máximo um professor"
c2 = model.addConstrs(x.sum('*', m, h, '*') <= 1 for m in materias for h in horarios)

"Em um determinado professor, horario e dia, terá no máximo uma matéria"
c3 = model.addConstrs(x.sum(p, '*', h, d) <= 1 for p in professores for h in horarios for d in dias)


# ====== Executa o modelo
model.optimize()

for p in professores:
    for m in materias:
        for h in horarios:
            for d in dias:
                if round(x[p, m, h, d].X) == 1:
                    print(p, m, h, d)
