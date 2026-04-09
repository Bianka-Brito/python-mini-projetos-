lista = [ ]
acima = [ ]

while True:
    print('-' * 20 + 'MENU' + '-' * 20)
    print('1-Adicionar notas \n2-Analise de dados \n3-Sair')
    print('-' * 44)
    menu= int(input('Digite uma opção: '))
    print('-' * 44)

    if menu == 1:
        num=int(input('Digite quantas notas você quer adicionar: '))
        print('-' * 44)
        for n in range(0,num):
            nota=int(input('Adicione uma nota: '))
            lista.append(nota)
            print('-' * 44)
        print('Todas as nota: ', lista)

    elif menu == 2:
        quant=len(lista)
        print('Quantidade de notas: ', quant)
        media= sum(lista) / len(lista)
        print('A média das notas é: ', media)
        for m in lista:
            if m > media: 
                acima.append(m)
                a=len(acima)
        print('Notas acima da media: ', a)
            
        maior = lista[0]
        menor= lista[0]
        for i in lista:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
        print('A maior nota é: ', maior)
        print('A menor nota é: ', menor)
            
    else: 
        break
