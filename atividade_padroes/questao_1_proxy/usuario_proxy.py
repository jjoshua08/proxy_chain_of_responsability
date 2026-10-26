from .usuario import DadosUsuario, Usuario


class UsuarioProxy(DadosUsuario):
    def __init__(self, usuario: Usuario):
        self.__usuario = usuario

    @property
    def nome(self) -> str:
        return self.__usuario.nome

    @property
    def cpf(self) -> str:
        cpf = self.__usuario.cpf
        total_digitos = sum(caractere.isdigit() for caractere in cpf)
        posicao = 0
        resultado = []
        for caractere in cpf:
            if caractere.isdigit():
                posicao += 1
                if posicao <= 3 or posicao > total_digitos - 2:
                    caractere = "*"
            resultado.append(caractere)
        return "".join(resultado)

    @property
    def endereco(self) -> str:
        raise PermissionError("Acesso ao endereço bloqueado pelo Proxy.")
