class MateriaClass:
    def __init__(self, nome: str, cargaHoraria: int, professor=None) -> None:
        self.__nome = nome
        self.__professor = professor
        self.__cargaHoraria = cargaHoraria

    def get_nome(self) -> str:
        return self.__nome

    def get_professor(self) -> str:
        return self.__professor

    def get_carga_horaria(self) -> int:
        return self.__cargaHoraria

    def set_nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            print('Dados inválidos')

    def set_professor(self, professor) -> bool:
        if self.__professor is None and professor is not None:
            self.__professor = professor
            return True
        elif professor is None:
            self.__professor = None
            return True
        else:
            return False

    def imprimir(self):
        print("Matéria: {} - Carga Horária: {} - Professor: {}".format(self.__nome, self.__cargaHoraria, self.__professor))
