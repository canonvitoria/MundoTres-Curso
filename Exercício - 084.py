id = []
fixa = []
men = 0
mai = 0
while True:
    id.append(str(input("Nome: ")))
    id.append(float(input("Peso: ")))
    if len(fixa) == 0:
        men = mai = id[1]
    else:
        if id[1] > mai:
            mai = id[1]
        if id[1] < men:
            men = id[1]
    fixa.append(id[:])
    id.clear()
    r = str(input("Quer continuar? [S/N]"))
    if r in 'Nn':
        break

print('-' * 30)
print(f'Ao todo, você cadastrou {len(fixa)} pessoas.')
print('-' * 30)
print(f'O maior peso foi de {mai}Kg. Peso de', end = ' ')
for p in fixa:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in fixa:
    if p[1] == men:
        print(f'{p[0]} ', end='')
print()
