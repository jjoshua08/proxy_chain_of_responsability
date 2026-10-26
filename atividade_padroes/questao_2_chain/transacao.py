from dataclasses import dataclass
from decimal import Decimal

from .conta import Conta


@dataclass
class Transacao:
    conta: Conta
    valor: Decimal
