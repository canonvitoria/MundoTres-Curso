num = [2, 5, 9, 1]
#Mudar o valor do número
num[2] = 3
#Adicionar valores
num.insert(2, 0)
num.append(7)
#Ordena ao contrario
num.sort(reverse=True)
#Eliminar elementos
num.pop(2)
num.remove(2)
#Impressão
print(num)
print(f'Essa lista tem {len(num)} elementos')
#-----------------------------------------------
if 4 in num:
    num.remove(4)
else:
    print(f'Não achei o número 4')
#----------------------------------------------
valores = []

valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encotrei o valor {v}...')
#---------------------------------------------
valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f'Na posição {c} encotrei o valor {v}...')
#---------------------------------------------
#Cópia de uma lista
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8