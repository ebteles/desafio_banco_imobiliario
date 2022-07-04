from .base_perfil import BasePerfil


class PerfilExigente(BasePerfil):
    def _roles_to_payment(self, patrimony):
        if patrimony.valor_aluguel > 50:
            self.pagamento(patrimony.custo_compra,
                           patrimony.tipo_estrategia)
            return True
        return False
