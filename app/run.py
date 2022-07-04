from config.configuracoes import Configuracoes

from tabuleiro.factory import criar_tabuleiro
from tabuleiro.exibir_resultados import exibir_resultados


def main():
    resultados = []
    for _ in range(int(Configuracoes.TOTAL_SIMULACOES)):
        tabuleiro = criar_tabuleiro()
        while tabuleiro.vencedor is None:
            for jogador in tabuleiro.jogadores:
                if jogador.gameover:
                    tabuleiro.remove(jogador)
                vencedor = tabuleiro.vendedor(jogador)
                if vencedor:
                    tabuleiro.vencedor = vencedor
                    break
                tabuleiro.jogar(jogador, tabuleiro)
            tabuleiro.contador += 1
        resultados.append(tabuleiro.fim())
    exibir_resultados(resultados)


if __name__ == "__main__":
    main()
