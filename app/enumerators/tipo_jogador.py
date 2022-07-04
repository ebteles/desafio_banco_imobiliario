from enum import Enum


class TipoJogador(str, Enum):
    IMPULSIVO = "Impulsivo"
    EXIGENTE = "Exigente"
    CAUTELOSO = "Cauteloso"
    ALEATORIO = "Aleatorio"
