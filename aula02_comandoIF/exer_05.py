a1 = float(input('Digite a altura da pessoa 1: '))
a2 = float(input('Digite a altura da pessoa 2: '))
a3 = float(input('Digite a altura da pessoa 3: '))

if a1 < a2 and a1 < a3:
    if a2 < a3:
        print(f'Ordem: p1: {a1}, p2: {a2}, p3: {a3}.')
    else:
        print(f'Ordem: p1: {a1}, p3: {a3}, p2: {a2}.')
if a2 < a1 and a2 < a3:
    if a1 < a3:
        print(f'Ordem: p2: {a2}, p1: {a1}, p3: {a3}.')
    else:
        print(f'Ordem: p2: {a2}, p3: {a3}, p1: {a1}.')
if a3 < a1 and a3 < a2:
    if a1 < a2:
        print(f'Ordem: p3: {a3}, p1: {a1}, p2: {a2}.')
    else:
        print(f'Ordem: p3: {a3}, p2: {a2}, p1: {a1}.')
