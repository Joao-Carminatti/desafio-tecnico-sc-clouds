def fibonacci(n):
    """
    Calcula o termo da posição N da sequência de Fibonacci de forma iterativa (linear).

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
        a, b = 0, 1
        for _ in range(2, n + 1):
            a,b = b, a + b
        return b

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(-3))

        