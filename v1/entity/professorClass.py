from v1.entity.materiaClass import MateriaClass


class ProfessorClass:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__materias = []

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print('Dados inválidos')

    def adicionar_materia(self, materia: MateriaClass) -> None:
        materia.set_professor(materia.get_professor())
        self.__materias.append(materia)

    def deletar_materia(self, materia: MateriaClass) -> None:
        response = materia.set_professor(None)
        if response:
            self.__materias.remove(materia)
            print('Matéria exluída com sucesso')
        else:
            print('Erro ao excluir matéria')

    def get_materias(self):
        return self.__materias

    def imprimir(self):
        print("Professor: {}.".format(self.__nome))
        for idx, materia in enumerate(self.__materias):
            materia.imprimir()


