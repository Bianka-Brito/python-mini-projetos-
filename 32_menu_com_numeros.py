numeros = [ ]

while True:
    print('1- Adicionar número \n2- Ver lista \n3- Mostrar maior \n4-Sair')
    menu= int(input('Escolha sua opção: '))
    
    if menu == 1:
        lista = int(input('Quantos números você quer adicionar? '))
        for l in range(0,lista): 
            n=input('Adicione um número: ')
            numeros.append(n)
    elif menu == 2:
        print(numeros)
    
    elif menu == 3:
        maior = numeros[0]
        for i in numeros:
            if i > maior:
                maior = i
        print(f'Maior número da lista é: {maior}')
    elif menu == 4:
        print('Saindo...') 
        break 
