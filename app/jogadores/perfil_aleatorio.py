from random import randint

from .base_perfil import BasePerfil


class PerfilAleatorio(BasePerfil):
    def _roles_to_payment(self, patrimony):
        if randint(0, 1) > 0:
            self.pagamento(patrimony.custo_compra,
                           patrimony.tipo_estrategia)
            return True
        return False
