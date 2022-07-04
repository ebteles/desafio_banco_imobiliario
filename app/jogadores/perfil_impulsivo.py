from .base_perfil import BasePerfil


class PerfilImpusivo(BasePerfil):
    def _roles_to_payment(self, patrimony):
        self.pagamento(patrimony.custo_compra, patrimony.tipo_estrategia)
        return True
