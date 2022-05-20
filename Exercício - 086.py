
números = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        números[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{números[l] [c]:^5}]', end='')
    print()



