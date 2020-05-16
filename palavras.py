'''frases = ['olar como vais','ahoy,tudo bão','aloha bebeês queridos']

for frase in sorted(frases):
    print(frase)

print(frases[0])

foods = {'pequi':'peekai','banana':'platano','maça':'pomme'}

palavra  = input("Qual a palavra vc gostaria de traduzir?\n").strip()
print(foods[palavra])'''

ingles = {'pipoca':'popcorn','pudim':'pudding'}
frances = {'pipoca':'pipoquê','pudim':'pudingy'}
espanhol = {'pipoca':'pochoclos','pudim':'postrecito'}

dicionario = {'ingles': ingles,'frances': frances, 'espanhol':espanhol}

palavra  = input("Qual a palavra vc gostaria de traduzir?\n").strip()
lingua = input("pra qual lingua?")

if lingua in dicionario and palavra in dicionario[lingua]:
    print(dicionario[lingua][palavra])

else:
    print(f'A lingua {lingua} ou a {palavra} não ta rolano.')


#Todo tratar Keyerror (lingua errada + palavra errada) + Ensinar Função
'''
if lingua == 'ingles':
    print(ingles[palavra])

elif lingua == 'frances':
    print(frances[palavra])

elif lingua == 'espanhol':
    print(espanhol[palavra])

else: 
    print("não tem.... fim")
'''