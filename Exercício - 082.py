lista = []
pares = []
ímpares = []

while True:
    lista.append(int(input("Digite um número: ")))
    r = str(input("Deseja continuar? [S/N]"))
    if r in "Nn":
        break
print('-' * 30)
print(f'A lista completa é {lista}')
print('-' * 30)
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
