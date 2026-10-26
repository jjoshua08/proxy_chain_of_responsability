from abc import ABC, abstractmethod
from decimal import Decimal

from .transacao import Transacao


class Validador(ABC):
    def __init__(self):
        self._proximo = None

    def definir_proximo(self, proximo: "Validador") -> "Validador":
        self._proximo = proximo
        return proximo

    def validar(self, transacao: Transacao) -> tuple[bool, str]:
        motivo = self.verificar(transacao)
        if motivo:
            return False, motivo
        if self._proximo is not None:
            return self._proximo.validar(transacao)
        return True, "Todas as validações foram aprovadas."

    @abstractmethod
    def verificar(self, transacao: Transacao) -> str:
        pass


class ValidadorSaldo(Validador):
    def verificar(self, transacao: Transacao) -> str:
        if transacao.conta.saldo < transacao.valor:
            return "Saldo insuficiente."
        return ""


class ValidadorLimite(Validador):
    def verificar(self, transacao: Transacao) -> str:
        limites = {"Comum": Decimal("1000.00"), "Premium": Decimal("10000.00")}
        limite = limites[transacao.conta.tipo]
        if transacao.valor > limite:
            limite_formatado = "1.000,00" if transacao.conta.tipo == "Comum" else "10.000,00"
            return f"Valor superior ao limite de R$ {limite_formatado} da conta {transacao.conta.tipo}."
        return ""


class ValidadorBloqueioJudicial(Validador):
    def verificar(self, transacao: Transacao) -> str:
        if transacao.conta.bloqueio_judicial:
            return "Conta com bloqueio judicial."
        return ""
