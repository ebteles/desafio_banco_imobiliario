import os
from collections import Counter
from typing import List

from model.resultado import Resultado


def exibir_resultados(lista_resultados: List[Resultado]) -> None:

    total_timeout = sum(
        [1 for resultado in lista_resultados if resultado.time_out])
    total_contador = sum(
        [resultado.contador for resultado in lista_resultados])
    count_vencedor = Counter()

    for resultado in lista_resultados:
        estrategia = str(resultado.estrategia)
        count_vencedor[estrategia] += 1

    os.system('cls' if os.name == 'nt' else 'clear')

    print(
        f'''{"-" * 80}\n'''
        f'''{str.center("RESULTADO", 80)}\n'''
        f'''{"-" * 80}\n'''
    )

    print(
        f'''1. Partidas terminadas por time out (1000 rodadas): '''
        f'''{total_timeout}'''
    )

    print(
        f'''2. Tempo médio de cada turno em uma partida: '''
        f'''{total_contador / len(lista_resultados):.1f}'''
    )

    print("3. Porcentagem de vitórias por comportamento dos jogadores")
    for estrategia, vencedor in count_vencedor.most_common():
        print(
            "  ",
            f"{estrategia}: {(vencedor * 100)// len(lista_resultados)}%"
        )

    print(
        f'''4. Comportamento vencedor:\n'''
        f'''   "{count_vencedor.most_common(1)[0][0]}"'''
        f''' com {count_vencedor.most_common(1)[0][1]} vitórias'''
        f'''\n{"-" * 80}\n'''
    )
