def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Media'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM!'
    return r

resp = notas(8.0, 8.5, 9, sit=True)
print(resp)