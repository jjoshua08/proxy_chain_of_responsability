from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Conta:
    tipo: str
    saldo: Decimal
    bloqueio_judicial: bool = False
