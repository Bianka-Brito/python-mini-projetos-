lista = [ ]
for i in range(0, 10):
    num= int(input(f'Digite o numero {i+1} para a lista: '))
    lista.append(num)
print(lista)
pares = [ ]
for l in lista:
    if l %2==0:
        pares.append(l)
print(f'Lista só com números pares: {pares}')
qt= len(pares)
print(f'Sua lista com números pares tem {qt} itens')
