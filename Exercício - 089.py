alunos = []

while True:
    nome = (str(input("Nome: ")))
    nota1 = (float(input("Nota1: ")))
    nota2 = (float(input("Nota2: ")))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    r = str(input("Deseja continuar? [S/N] "))
    if r in 'Nn':
        break

print('-' * 50)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 50)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:>10}{a[2]:>8}')
print('-' * 50)

while True:
    p = int(input('Mostrar a nota de qual aluno? [999 interrompe]'))
    if p == 999:
        print('Finalizando...')
        break
    if p <= len(alunos) - 1:
        print(f'Notas de {alunos[p] [0]} são {alunos[p] [1]}')
print("VOLTE SEMPRE!!!")