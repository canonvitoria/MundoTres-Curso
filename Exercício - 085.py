valores = [[], []]

print('-' * 40)

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
n4 = int(input("Digite o quarto valor: "))
n5 = int(input("Digite o quinto valor: "))
n6 = int(input("Digite o sexto valor: "))
n7 = int(input("Digite o sétimo valor: "))

print('-' * 40)
for n in range(1, 7):
    if n % 2 == 0:
        valores[0].append(n)
    if n % 2 == 1:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')