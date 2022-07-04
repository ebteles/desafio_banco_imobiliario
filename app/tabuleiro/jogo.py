from datetime import datetime
from random import randint
from model.resultado import Resultado

from config.configuracoes import Configuracoes

from .propriedade import Propriedade


class Jogo:

    def __init__(self, *args, **kwargs):
        self._vencedor = None
        self._contador = 0
        self._jogadores = []
        self.inicio = datetime.now()
        self._cards = [
            Propriedade(index, None)
            for index in range(
                int(Configuracoes.TOTAL_PROPRIEDADES)
            )
        ]

    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self, contador):
        self._contador = contador

    @property
    def jogadores(self):
        return self._jogadores

    @jogadores.setter
    def jogadores(self, jogadores):
        self._jogadores = jogadores

    @property
    def vencedor(self):
        return self._vencedor

    @vencedor.setter
    def vencedor(self, vencedor):
        self._vencedor = vencedor

    @property
    def jogar_dado(self):
        return randint(1, 6)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, patrimony):
        self._cards[position] = patrimony

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"{self._cards}"

    def __repr__(self):
        return f"{self._cards}"

    def remove(self, player):
        for patrimony in self._cards:
            if patrimony.tipo_estrategia == player:
                patrimony.tipo_estrategia = None
        self._jogadores.remove(player)

    def jogada(self, player, _dice=None):
        goto = player.position + (_dice or self.jogar_dado)
        if goto >= int(Configuracoes.TOTAL_PROPRIEDADES):
            player.saldo += float(Configuracoes.SALDO_POR_VOLTA)
            goto -= int(Configuracoes.TOTAL_PROPRIEDADES)
        player.position = goto
        return goto

    def vendedor(self, player):
        if len(self.jogadores) == 1:
            return player
        if int(Configuracoes.MAXIMO_JAGADAS) <= self.contador:
            saldo = 0
            vencedor = None
            for _player in self._jogadores:
                if _player.saldo > saldo:
                    saldo = _player.saldo
                    vencedor = _player
            return vencedor

        elements = [
            _player.saldo
            for _player in self._jogadores if _player != player
        ]
        if sum(elements) < 0:
            return player

        return None

    def jogar(self, player, board):
        if player.saldo <= 0:
            player.gameover = True
            return

        patrimony = self._cards[self.jogada(player)]
        player.alugar_ou_comprar(patrimony, board)

    def fim(self):
        resultado = Resultado(
            tempo=(datetime.now() - self.inicio).total_seconds(),
            vencedor=str(self.vencedor),
            saldo=self.vencedor.saldo,
            contador=self.contador,
            estrategia=str(self.vencedor),
            time_out=self.contador > int(Configuracoes.MAXIMO_JAGADAS)
        )
        return resultado
