"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""
from os import system
if system("clear") != 0: system("cls")


def execute_battle(list_a, list_b):
    n = len(list_a)
    for idx in range(n):
        if list_a[idx] != list_b[idx]:
            dif = abs(list_a[idx] - list_b[idx])
            if list_a[idx] < list_b[idx]:
                if idx + 1 < n:
                    list_b[idx + 1] += dif
                else:
                    return f"{dif}b"
            else:
                if idx + 1 < n:
                    list_a[idx + 1] += dif
                else:
                    return f"{dif}a"
    return "x"

lista_a = [5, 3, 3]
lista_b = [4, 4, 2]

print(execute_battle(lista_a, lista_b))
