from random import randint


class Propriedade:

    def __init__(self, id, tipo_estrategia=None, *args, **kwargs):
        self.id = id
        self.tipo_estrategia = tipo_estrategia
        self.valor_aluguel = randint(30, 120)
        self.custo_compra = randint(30, 120)

    def __repr__(self):
        return f'''
            id:{self.id}
            tipo_estrategia:{self.tipo_estrategia}
            valor_aluguel:{self.valor_aluguel}
            custo_compra:{self.custo_compra}
        '''

    def __str__(self):
        return f'''
            id:{self.id}
            tipo_estrategia:{self.tipo_estrategia}
            valor_aluguel:{self.valor_aluguel}
            custo_compra:{self.custo_compra}
        '''
