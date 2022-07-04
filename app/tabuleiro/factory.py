from config.configuracoes import Configuracoes
from enumerators.tipo_jogador import TipoJogador
from jogadores.perfil_cauteloso import PerfilCauteloso
from jogadores.perfil_exigente import PerfilExigente
from jogadores.perfil_impulsivo import PerfilImpusivo
from jogadores.perfil_aleatorio import PerfilAleatorio

from .jogo import Jogo

estrategias = {
    TipoJogador.IMPULSIVO: PerfilImpusivo,
    TipoJogador.EXIGENTE: PerfilExigente,
    TipoJogador.CAUTELOSO: PerfilCauteloso,
    TipoJogador.ALEATORIO: PerfilAleatorio,
}


def iniciar_jogo(estrategia: str, *args, **kwargs):
    try:
        return estrategias[estrategia](estrategia=estrategia, *args, **kwargs)

    except KeyError:
        estrategias_disponiveis = ", ".join(estrategias.keys())
        raise NotImplementedError(
            f"Estratégia '{estrategia}' não implementada."
            f"Favor selecionar uma das estratégias disponíveis: {estrategias_disponiveis}"
        )


def criar_tabuleiro():
    tabuleiro = Jogo()
    jogadores = [
        iniciar_jogo(estrategia) for estrategia in Configuracoes.COMPORTAMENTO
    ]
    tabuleiro.jogadores = jogadores
    return tabuleiro
