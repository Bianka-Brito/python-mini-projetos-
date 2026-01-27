def verificar_media(media):
    if media <5:
        return 'reprovado'
    elif 5 <= media <= 6.9:
        return 'recuperação'
    else:
        return 'aprovado'
media= float(input('Digite uma nota: '))
nota= verificar_media(media)
print(nota)
