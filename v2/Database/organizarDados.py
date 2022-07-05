from v1.entity import MateriaClass, ProfessorClass
import pandas as pd


class Dados:

    @staticmethod
    def organizarDados():
        dataProfessor = pd.read_csv('Database/professor.csv', sep=',')
        dataMateria = pd.read_csv('Database/materia.csv', sep=',')

        vet_professores = list(dataProfessor.values.base[0])
        vet_materia_nome = list(dataMateria.values.base[0])
        vet_materia_professor = list(dataMateria.values.base[1])
        vet_materia_carga = list(dataMateria.values.base[2])
        horarios = ['18h', '19h', '20h', '21h', '22h']
        dia = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
        dia_horario = dict()
        for i in dia:
            dia_horario[i] = horarios

        listProfessor = []
        for idx, professor in enumerate(vet_professores):
            listProfessor.append(professor)

        prof_materia = dict()
        carga = dict()
        listMateria = []
        for idx, materia in enumerate(vet_materia_nome):
            prof_materia[materia] = vet_materia_professor[idx]
            carga[materia] = vet_materia_carga[idx]
            listMateria.append(materia)

        return prof_materia, horarios, carga, listMateria, listProfessor, dia, dia_horario
