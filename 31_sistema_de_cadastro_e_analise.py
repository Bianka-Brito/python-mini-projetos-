print('Python para iniciantes', 3, 60)
print('\n---------------------------------')
participantes= [{'Nome': 'Bianka', 'Idade': 24, 'Horas de estudo': 10, 'Area de interesse': 'Dados'},
                {'Nome': 'Lua', 'Idade': 20, 'Horas de estudo': 8, 'Area de interesse': 'Java'},
                {'Nome': 'Liz', 'Idade': 30, 'Horas de estudo': 12, 'Area de interesse': 'TI'}]
while True:
    print('1.Cadastrar participante \n2.Mostrar participantes \n3.Mostrar análises \n4.Sair')
    print('---------------------------------')
    menu = input('Escolha sua opção: ')
    print('\n---------------------------------')
    if menu == '1': 
        nome = input('Insira o nome da participante: ')
        idade = int(input('Insita a idade da participante: '))
        horas_de_estudo= int(input('Quantas horas essa participante estuda por semana: '))
        area_de_interesse = input('Qual a aréa de interesse da participante: ')
        novo = {'Nome': nome, 'Idade': idade, 'Horas de estudo': horas_de_estudo, 'Area de interesse': area_de_interesse}
        participantes.append(novo)
        for p in participantes:
          print(p)
        print('\n---------------------------------')
    
    elif menu == '2':
        for p in participantes:
            print(p)
        print('-'* 90)
    
    elif menu == '3':
        maiores = 0
        soma_horas = 0
        estudos = [ ]
        total = [ ]
        for i in participantes:
            soma_horas += i['Horas de estudo']
            if i['Nome']: 
                total.append(i['Nome'])
                t = len(total)
            if i['Idade'] >= 18: 
                maiores +=1
            if i['Horas de estudo'] >= 5:
                estudos.append(i['Nome']) 
                
        media = soma_horas / t
        print(f'-------- Análise de dados -------- \n--------------------------------- \nTotal de participantes: {t} \nMaiores de idade: {maiores} \nMédia horas de estudos: {media} \nParticipantes com bom ritmo de estudos (>= 5h):{estudos} \n\n---------------------------------')
    
    else:
        break
