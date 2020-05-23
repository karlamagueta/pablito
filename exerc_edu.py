# print('SantiaelCodes, muito thanks pelo subs, coração! Uhuuuul')


import random 

def subs_maravilhosos(nome_sub):
    '''essa funcción irá mandar uma msg random de agradecimento'''  
    thanks =[
        'Muito thanks, coração',
        'Aiiii que lindeza, obrigada',
        'Valeuuuuzis',
        'Merci mon amouuuuuuuuurrrrrrrrrr (com biquinho)',
        'Gracias tchutchuquite',
        'sogtouDANKENbcjlxoocbgste (obrigada em alemão)'
    ]

    agradecimento = random.choice(thanks)
    return f'{nome_sub}, {agradecimento}'

#nome_sub = input('Qual o nome do sub?')
subs =[
   'SantiaelCodes',
   'Codeshow',
   'SpaceDevs',
   'bruno001',
   'Ander_viega',
   'cfreitas'
]

for nome_sub in subs:
    print(subs_maravilhosos(nome_sub))
        
        
        
