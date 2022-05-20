soma = 0
soma3 = 0
mai = 0
menor = 0
números = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        números[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{números[l] [c]:^5}]', end = '')
        if números[l][c] % 2 == 0:
            soma += números[l] [c]
    print()
print('-' * 30)
print(f'A soma dos valores pares é {soma}')
for l in range(0, 3):
    soma3 += números[l][2]
print(f'A soma dos valores da terceira camada é {soma3}')
for c in range (0, 3):
    if c == 0:
        mai = números[1][c]
    elif números[1][c] > mai:
        mai = números[1] [c]
print(f'O maior valor da segunda linha é {mai}')