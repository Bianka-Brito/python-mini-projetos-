def max(entrada): 
    return lista.sort()
entrada = int(input('Digite quantos numeros tera na sua lista: '))
lista = []
for i in range(entrada):
    l = input(f'digite o numero {i+1} da lista: ')
    lista.append(l)
print(lista)
print(f'O maior numero da sua lista é: {lista[-1]}')
