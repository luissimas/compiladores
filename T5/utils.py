#!/usr/bin/env python3


def is_coercible(type_a, type_b):
    """Verifica se o tipo type_a pode ser coercido para o tipo type_b.

    Essa função verifica se o tipo type_a pode ser coercido (convertido) para o tipo type_b.
    Se type_a for "real" e type_b for "inteiro", ela retorna True, indicando que type_a pode ser coercido para type_b.
    Caso contrário, ela retorna o resultado da comparação entre type_a e type_b, ou seja, retorna True se eles forem do mesmo tipo e False caso contrário.

    Args:
        type_a (str): O primeiro tipo a ser verificado.
        type_b (str): O segundo tipo a ser verificado.

    Returns:
        bool: True se type_a for "real" e type_b for "inteiro", indicando que type_a pode ser coercido para type_b.
              Caso contrário, retorna o resultado da comparação entre type_a e type_b.

    Exemplos:
        >>> is_coercible("real", "inteiro")
        True
        >>> is_coercible("inteiro", "inteiro")
        True
        >>> is_coercible("real", "string")
        False
    """
    if type_a == "real" and type_b == "inteiro":
        return True

    if type_a == "inteiro" and type_b == "real":
        return True

    if type_a == "ponteiro" and type_b == "endereco":
        return True

    return type_a == type_b


def flatten_list(nested_list):
    """Aplanar uma lista aninhada.

    Essa função recebe uma lista aninhada como argumento e retorna uma versão aplanada (flatten) da lista.
    Ela itera sobre cada item da nested_list e verifica se o item é uma lista.
    Se o item for uma lista, a função chama recursivamente a função flatten_list para aplanar essa lista.
    Caso contrário, o item é adicionado à lista aplanada.

    Args:
        nested_list (list): A lista aninhada a ser aplanada.

    Returns:
        list: Uma versão aplanada da lista aninhada.

    Exemplos:
        >>> flatten_list([1, [2, [3, 4], 5], 6])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_list([7, 8, 9])
        [7, 8, 9]
        >>> flatten_list([[10, 11], [12, [13, 14]], 15])
        [10, 11, 12, 13, 14, 15]
    """
    flattened = []

    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)

    return flattened
