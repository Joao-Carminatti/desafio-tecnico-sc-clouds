def num_primo(n):
    """
    Verifica se um número é primo, chamando a função auxiliar recursiva
    que testa os divisores um por um a partir de d=2.

    Args:
        n (int): número a ser verificado

    Returns:
        bool: True se n for primo, False caso contrário
    """
    if n < 2:
        return False
    return num_primo_aux(n, 2)


def num_primo_aux(n, d):
    """
    Função auxiliar recursiva que testa se 'd' é divisor de 'n'.
    Avança d+1 a cada chamada até encontrar um divisor ou até d == n.

    Args:
        n (int): número sendo testado
        d (int): divisor atual sendo testado

    Returns:
        bool: True se nenhum divisor foi encontrado (n é primo),
              False se algum divisor foi encontrado
    """
    if d == n:
        return True
    if n % d == 0:
        return False
    return num_primo_aux(n, d + 1)


def primos_ate_n(n):
    """
    Retorna todos os números primos entre 2 e n (inclusive), de forma recursiva.

    Args:
        n (int): limite superior do intervalo (n > 1)

    Returns:
        list[int]: lista com todos os números primos até n
    """
    return primos_ate_n_aux(n, 2)


def primos_ate_n_aux(n, atual):
    """
    Função auxiliar recursiva que percorre os números de 'atual' até 'n',
    somando à lista os que forem primos.

    Args:
        n (int): limite superior do intervalo
        atual (int): número atual sendo avaliado nesta chamada

    Returns:
        list[int]: lista com os primos encontrados a partir de 'atual' até n
    """
    if atual > n:
        return []
    if num_primo(atual):
        return [atual] + primos_ate_n_aux(n, atual + 1)
    else:
        return primos_ate_n_aux(n, atual + 1)

print(num_primo(1))
print(num_primo(2))
print(num_primo(3))
print(num_primo(4))
print(num_primo(5))
print(primos_ate_n(10))