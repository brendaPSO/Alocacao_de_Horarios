import pandas as pd


class Dados:

    @staticmethod
    def organizarDados():
        dataProfessor = pd.read_csv('Database/professor.csv', sep=';')
        dataMateria = pd.read_csv('Database/materia.csv', sep=',')
        vet_professores = list(dataProfessor.values.base[0])
        vet_materia_nome = list(dataMateria.values.base[0])
        vet_materia_professor = list(dataMateria.values.base[1])
        vet_materia_carga = list(dataMateria.values.base[2])
        horarios = ['18h', '19h', '20h', '21h', '22h']
        dia = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

        dataDia = open('Database/dia.txt', 'r')
        linhas = dataDia.readlines()
        dataDia.close()

        prof_dia = dict()
        campos = list()
        i = 0
        for linha in linhas:
            if linha == "\n":
                continue
            campos.append(linha.replace("\n", "").split(","))
            if (i+1) % 5 == 0:
                prof_dia[vet_professores[(i/5).__trunc__()]] = campos.copy()
                campos.clear()
            i = i+1

        prof_materia = dict()
        carga = dict()
        listMateria = []
        for idx, materia in enumerate(vet_materia_nome):
            prof_materia[materia] = vet_materia_professor[idx]
            carga[materia] = vet_materia_carga[idx]
            listMateria.append(materia)

        return prof_materia, horarios, carga, listMateria, vet_professores, dia, prof_dia
