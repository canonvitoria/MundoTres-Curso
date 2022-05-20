#Impressão somente do suco que foi o último a ser adicionado
lanche = ("Hambúrguer")
lanche = "Suco"
print(lanche)

#Mostra todos
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche)

#Mostra o suco
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche[2])

#Mostra a pizza
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche[-3])

#Mostra o suco e a pizza
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche[1:3])

#Mostra do dois ao final
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche[2:])

#Mostra do inicio até o elemento dois, cortando o elemento dois
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche[:2])

#Maneira mais organizada
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
for c in lanche:
    print(f"Eu vou comer {c}")
print("Comi AFU!!")
      #Ou
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
for cont in range(0, len(lanche)):
    print(lanche[cont])

#Mostrar a posição
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

#Mostra em ordem
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(sorted(lanche))

#Soma das tuplas e cria a tupla c
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

#Quantas vezes está aparecendo tal número aparece dentro de C
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))

#Mostra a posição
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8))

#Diferentes dados
pessoa = ("Gustavo", 19, "M", 70)
print(pessoa)