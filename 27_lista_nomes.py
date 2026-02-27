qt= [ ]
while True:
    nome= input("Digite um nome (Para encerrar digite 'sair'): ")
  
    if nome == 'sair':
        break
    else: 
        qt.append(nome)
print(qt)

total = 0
for i in qt:
    total +=1
print(f'Sua lista tem: {total} nomes')
print(f'O primeiro nome da sua lista é: {qt[0]} \nO ultimo nome da sua lista é: {qt[-1]}')
