from dataclasses import dataclass


@dataclass
class Resultado:

    tempo: float
    vencedor: str
    saldo: float
    contador: int
    estrategia: str
    time_out: bool
