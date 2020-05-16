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

try:
    print(dicionario[lingua][palavra])
except KeyError:
    print('deu ruim fuen fuen fuen')