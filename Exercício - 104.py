def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt("Digite um número: ")
print(f"Voce digitou o número {n}")