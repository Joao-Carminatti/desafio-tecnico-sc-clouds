def fibonacci(n):
    """
    Calcula o termo da posição N da sequência de Fibonacci de forma recursiva.

    A função chama a si mesma somando os dois termos anteriores
    (fib(n-1) + fib(n-2)) até atingir os casos base (n=0 ou n=1).

    Args:
        n (int): posição desejada na sequência (n >= 0)

    Returns:
        int: valor de fib(n)
        str: mensagem de erro se n for negativo
    """
    if n < 0:
        return "Regra da soma não se aplica para números negativos ou zero!"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(-3))