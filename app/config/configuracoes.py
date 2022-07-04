from enumerators.tipo_jogador import TipoJogador


class Configuracoes:
    COMPORTAMENTO = [
        TipoJogador.IMPULSIVO,
        TipoJogador.EXIGENTE,
        TipoJogador.CAUTELOSO,
        TipoJogador.ALEATORIO
    ]
    MAXIMO_JAGADAS = 1000
    SALDO_INICIAL = 300.0
    SALDO_POR_VOLTA = 100.0
    TOTAL_PROPRIEDADES = 20
    TOTAL_SIMULACOES = 300
