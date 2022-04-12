class usuario:
    contador = None

    def __init__(self: object, nome: str, cpf: float, datanascimento: float, Idade: int) -> usuario:
        self.datanascimento = datanascimento
        self.__nome: str = nome
        self.__cpf: float = cpf
        self.__idade: int = idade
        usuario.contador += 1

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self: object) -> float:
        return self.__cpf

    @property
    def datanascimento(self: object) -> float:
        return self.__datanascimento

    @property
    def idade(self: object) -> float:
        return self.__idade


class Usuario:
    pass
