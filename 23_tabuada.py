num= int(input("Digite um numero:"))
print(f'A tabuada no {num} é:')
for n in range(11):
    resul= n * num
    print(f'{n} X {num} = {resul}')
