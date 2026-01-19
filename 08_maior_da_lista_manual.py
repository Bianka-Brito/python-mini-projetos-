lista = [20, 30, 50, 25]
maior = lista[0] #começa assumindo que o primeiro é maior
for n in lista: #percorre a lista 
   if n > maior: #se n for maior que o maior, maior é igual a n (troca se outro numero for maior que o primeiro)
      maior = n
print(maior)
