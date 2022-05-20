def soma(a, b):
    s = a + b
    print(s)


soma(4, 5) #Substituição
A = 4
B = 5
S = A + B
print(S)

soma(8, 9) #Substituição
A = 8
B = 9
S = A + B
print(S)

soma(2, 1) #Substiytuição
A = 2
B = 1
S = A + B
print(S)

#-------------------------------------

def soma(a, b):
    s = a + b
    print(s)

soma(a = 4, b =4)

#------------------------------------

def soma(a, b):
    print(f'A = {A} e B = {B}')
    s = a + b
    print(s)
    print(f'A soma A + B = {S}')


soma(4, 5)

#-----------------------------------

valores = [6, 3, 9, 1, 0, 2]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


dobra(valores)
print(valores)

#----------------------------------

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {S}')


soma(5, 2)
soma(2, 9, 4)