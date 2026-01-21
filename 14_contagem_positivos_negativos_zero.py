numeros=[10,-5,0,7,-3,0,2]
positivos= [p for p in numeros if p > 0] 
pos= len(positivos)
negativos= [n for n in numeros if n < 0 ]
neg= len(negativos)
zero= [z for z in numeros if z == 0]
zr= len(zero)
print(numeros)
print(f'Nessa lista tem: {pos} números positivos \nNessa lista tem: {neg} números negativos \nNessa lista tem: {zr} números 0')
