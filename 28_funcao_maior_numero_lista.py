def maior_lista(lista):
    maior= lista[0] 
    for c in lista:
        if c > maior:
            maior=c
    return maior
entrada = int(input('Digite quantos numeros tera na sua lista: '))
lista = []
for i in range(entrada):
    num = int(input(f'digite o numero {i+1} da lista: '))
    lista.append(num)
print(lista)
resultado = maior_lista(lista)
print(resultado)
