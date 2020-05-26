#pgm que calcula a media de uma listaaaaaaaaa :D

numeros = list(range(0,100))

def media(numeros):
    media = sum(numeros)/len(numeros)
    return media

print (media(numeros))