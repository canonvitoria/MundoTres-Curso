numeros = (int(input("Digite um número: ")),
           int(input("digite outro número: ")),
           int(input("digite mais número: ")),
           int(input("digite último número: ")))

print('=' * 50)

print(f'Você digitou os valores: {numeros}')

print('=' * 50)

print(f'O número 9 apareceu {numeros.count(9)} vezes.')

print('=' * 50)

if 3 in numeros:
    print(f"O número 3 foi digitado na {numeros.index(3)+1} posição")
else:
    print("O número 3 apareceu em nenhuma posição")

print('=' * 50)

print("Os valores pares são: ", end = '')
for n in numeros:
    if n % 2 == 0:
        print(n, end = ' ')