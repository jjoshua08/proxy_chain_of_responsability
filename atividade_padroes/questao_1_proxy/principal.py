from .usuario import Usuario
from .usuario_proxy import UsuarioProxy


class Principal:
    @staticmethod
    def main():
        usuario = Usuario("Ana Silva", "123.456.789-01", "Rua das Flores, 100")
        proxy = UsuarioProxy(usuario)

        print(f"Nome: {proxy.nome}")
        print(f"CPF: {proxy.cpf}")
        try:
            print(f"Endereço: {proxy.endereco}")
        except PermissionError as erro:
            print(erro)


if __name__ == "__main__":
    Principal.main()
