def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

#-------------------------------------------------------
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultadosa são {f1}, {f2}, {f3}')

#------------------------------------------------------
def par (n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input("Digite um número:"))
print(par(n))

#-------------------------------------------------------
