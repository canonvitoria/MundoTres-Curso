times = ('Bragantino', 'Atlético-MG', 'Santos', 'Cuiabá', 'Corinthians',
         'América-MG', 'Internacional', 'Avaí', 'Palmeiras', 'Flamengo',
         'Botafogo', 'Coritiba', 'São Paulo', 'Fluminense', 'Ceára-SC',
         'Atlético-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')

print("============ LISTA DE TIMES DO BRASILEIRÃO 2022 ===========")
for t in times:
    print(t)
print("=" * 290)

print(f"Os 5 primeiros times do Brasileirão 2022 são: {times[0:5]}")
print("=" * 290)

print(f"Os 4 últimos times do Brasileirão 2022 são: {times[16:20]}")
print("=" * 290)

print("Os times do Brsileirão 2022 em ordem arfabética: ", end= '')
print(sorted(times))
print("=" * 290)

print("O time da Chapecoense não está nas colocações")
print("=" * 30)