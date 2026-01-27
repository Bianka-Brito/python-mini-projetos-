def verificar_nota(nota):
    if  0 <= nota  <= 10:
        return 'Valido'
    else: 
        return 'Invalido'
        
nota=int(input("Digite uma nota(número inteiro): "))
resultado = verificar_nota(nota)
print(resultado)
