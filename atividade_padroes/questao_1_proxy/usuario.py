from abc import ABC, abstractmethod


class DadosUsuario(ABC):
    @property
    @abstractmethod
    def nome(self) -> str:
        pass

    @property
    @abstractmethod
    def cpf(self) -> str:
        pass

    @property
    @abstractmethod
    def endereco(self) -> str:
        pass


class Usuario(DadosUsuario):
    def __init__(self, nome: str, cpf: str, endereco: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def endereco(self) -> str:
        return self.__endereco
