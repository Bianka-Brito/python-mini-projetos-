frase= input('Digite uma palavra: ')
palavras= frase.split()
contador= {}
for p in palavras: 
    contador[p] = contador.get(p, 0)+1
print(f'No seu texto as palavras se repetem {contador} vezes')
