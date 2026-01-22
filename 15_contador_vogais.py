palavra= str(input('Digite uma palavra ou um texto: ')).lower()
contador= 0

for char in palavra: 
    if char in 'aeiou':
        contador +=1
        
print(f'Total de vogais: {contador}')
