num=int(input('Digite um numero: '))
fat = 1
for i in range(1,num+1): #+1 para o numero do usuario entrar no loop, se não para 1 numero antes
    fat*=i
print(f'O fatorial do número {num} é: {fat}')
