texto=input('Digite seu texto')
print(f'Seu texto é: {texto}')
invertido= ' '.join(texto[::-1] for texto in texto.split()) 
print(invertido)
