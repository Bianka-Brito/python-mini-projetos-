cont = [ ]
for i in range(0, 5):
    lista= int(input('digite uma seguencia de numeros: '))
    cont.append(lista)
maior= cont[0]
menor= cont[0]
for c in cont:
    if c > maior: 
        maior = c
    if c < menor:
        menor=c
print(f'O maior numero é {maior} e o menor é {menor}')
