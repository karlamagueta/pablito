import random

print('Pablo, qual é a musica?')

musics = [
    'baby shark',
    'chan chan',
    'meu pintinho amarelinho',
    'lasanha',
    'merda virou coxinha',
    'salompas'
]

musica_escolhida = random.choice(musics)
musica_2 = random.choice(musics)
print(f'Pablo diz: As musicas saum {musica_escolhida}, e {musica_2}')

print(random.sample(musics,2))


