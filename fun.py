def gritar(texto,n=1):
    '''essa função transforma o txt em maisculo e repete N vezes'''
    texto_em_maisculo1 = texto.upper()
    texto_coisado = texto_em_maisculo1[::-1]
    return f'{texto_em_maisculo1} {texto_coisado} !!!!!!!!! ' * n
    
texto_gritado = gritar('Obrigada Spacedevs',2)
print(texto_gritado)

def desincravincavador(texto):
    '''recebe um txt "pneumoultramicroscopicossilicovulcanoconiótico" => "p44o"'''
    primeira_letra = texto[0]
    ultima_letra = texto[-1]
    tamanho_tot = len(texto) - 2
    return f'{primeira_letra}{tamanho_tot}{ultima_letra}'

print(desincravincavador('pneumoultramicroscopicossilicovulcanoconiótico'))
print(desincravincavador("KarlaMaguetaSoler"))
print(desincravincavador(42))

#Terminar de ver functions e exercicicicicicicos 
#modulos