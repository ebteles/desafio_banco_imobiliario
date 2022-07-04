from .base_perfil import BasePerfil


class PerfilCauteloso(BasePerfil):
    def _roles_to_payment(self, patrimony):
        if (self.saldo - patrimony.custo_compra) >= 80:
            self.pagamento(patrimony.custo_compra,
                           patrimony.tipo_estrategia)
            return True
        return False
