from abc import ABC, abstractmethod
from config.configuracoes import Configuracoes


class BasePerfil(ABC):

    def __init__(
        self, estrategia, position=0,
        saldo=Configuracoes.SALDO_INICIAL
    ):
        self.position = position
        self.saldo = saldo
        self.estrategia = estrategia
        self.gameover = False

    def __str__(self):
        return f"{self.estrategia}"

    def __repr__(self):
        return f"{self.estrategia}"

    def alugar_ou_comprar(self, patrimony, board=None):
        if patrimony.tipo_estrategia:
            if self != patrimony.tipo_estrategia:
                self.pagamento(patrimony.valor_aluguel,
                               patrimony.tipo_estrategia)
            return

        if self._roles_to_payment(patrimony):
            patrimony.tipo_estrategia = self

    @abstractmethod
    def _roles_to_payment(self, patrimony, board):
        raise NotImplementedError()

    def pagamento(self, custo_compra, tipo_estrategia=None):
        self.saldo -= custo_compra
        if tipo_estrategia:
            tipo_estrategia.saldo += custo_compra
        if not self.saldo:
            self.gameover = True
