expr = str(input("Digite uma expressão: "))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else: pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressão está certa!!')
else:
    print('Sua expressão está errada!!')

