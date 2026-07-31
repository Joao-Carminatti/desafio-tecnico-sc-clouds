def num_primo(n):
    """
    Verifica se um número é primo, testando divisores de forma iterativa (linear).

    Args:
        n (int): número a ser verificado

    Returns:
        bool: True se n for primo, False caso contrário
    """
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def primos_ate_n(n):
    """
    Retorna todos os números primos entre 2 e n (inclusive), de forma iterativa (linear).

    Percorre cada número do intervalo e reaproveita a função num_primo
    para testar sua primalidade.

    Args:
        n (int): limite superior do intervalo (n > 1)

    Returns:
        list[int]: lista com todos os números primos até n
    """
    lista_primos = []
    for numero in range(2, n + 1):
        if num_primo(numero):
            lista_primos.append(numero)
    return lista_primos

print(num_primo(1))
print(num_primo(2))
print(num_primo(3))
print(num_primo(4))
print(num_primo(5))
print(primos_ate_n(10))