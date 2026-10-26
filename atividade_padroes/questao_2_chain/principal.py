from decimal import Decimal

from .conta import Conta
from .transacao import Transacao
from .validadores import ValidadorBloqueioJudicial, ValidadorLimite, ValidadorSaldo


class Principal:
    @staticmethod
    def main():
        cadeia = ValidadorSaldo()
        cadeia.definir_proximo(ValidadorLimite()).definir_proximo(ValidadorBloqueioJudicial())

        simulacoes = [
            ("Transação aprovada", Conta("Comum", Decimal("2000.00")), Decimal("500.00")),
            ("Saldo insuficiente", Conta("Comum", Decimal("100.00")), Decimal("500.00")),
            ("Limite da conta Comum", Conta("Comum", Decimal("5000.00")), Decimal("1000.01")),
            ("Limite da conta Premium", Conta("Premium", Decimal("20000.00")), Decimal("10000.01")),
            ("Bloqueio judicial", Conta("Premium", Decimal("20000.00"), True), Decimal("500.00")),
        ]

        for descricao, conta, valor in simulacoes:
            aprovada, motivo = cadeia.validar(Transacao(conta, valor))
            resultado = "APROVADA" if aprovada else "REJEITADA"
            print(f"{descricao}: {resultado} — {motivo}")


if __name__ == "__main__":
    Principal.main()
