from entity import MateriaClass, ProfessorClass
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

        listProfessor = []
        for idx, professor in enumerate(vet_professores):
            obj = ProfessorClass(professor)
            listProfessor.append(obj)

        listMateria = []
        for idx, materia in enumerate(vet_materia_nome):
            obj = MateriaClass(materia, vet_materia_carga[idx], vet_materia_professor[idx])
            if vet_materia_professor[idx] is not None:
                for i, prof in enumerate(listProfessor):
                    if prof.get_nome() == vet_materia_professor[idx].strip():
                        prof.adicionar_materia(obj)
            listMateria.append(obj)

        rotulo_m = ["{}".format(valor.get_nome()) for idx, valor in enumerate(listMateria)]

        materias = dict()
        for idx, valor in enumerate(rotulo_m):
            materias[valor] = 1

        carga_horaria = dict()
        for idx, valor in enumerate(listMateria):
            carga_horaria[valor.get_nome()] = valor.get_carga_horaria()

        professores = dict()
        for i, prof in enumerate(listProfessor):
            professores[prof.get_nome()] = []
            listM = prof.get_materias()
            for j, valor in enumerate(listM):
                professores[prof.get_nome()].append(valor.get_nome())

        return materias, carga_horaria, professores, horarios
