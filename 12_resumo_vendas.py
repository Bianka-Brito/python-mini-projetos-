lista= [120,90,150,80,200]
total= sum(lista)
media= int(sum(lista) / len(lista))
lista.sort()
print(f'Total de vendas: {total},00')
print(f'A media das vendas é: {media},00')
print(f'A maior venda foi: {lista[-1]},00')
