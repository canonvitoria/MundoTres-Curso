lista = []
l = 0
while True:
        lista.append(int(input("Digite um valor: ")))
        r = str(input("Quer continuar? [S/N]"))
        if r in 'Nn':
            break
print('-' * 30)
print(f'Você digtou {len(lista)+1} elementos')
print('-' * 30)
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
print('-' * 30)
if 5 in lista:
    print("O número 5 foi digitado na lista")
else:
    print("O número 5 não foi digitado na lista")
print('-' * 30)
print("FIM DO PROGRAMA!")