estoque= {'Tenis':10, 'Blusa':50, 'Casaco':20}
estoque['Tenis']= 20
estoque['Blusa']= 30
estoque.update({'Tenis':30})
estoque.update({'Meia':40})
print(f'O estoque final é: {estoque}')
