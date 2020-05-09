music = []
#TODO: arrumar linhas 6 7 8 :)
resposta = input("Pablo, qual é a musica?")
continuar = 'sim'
while continuar == 'sim':
    add_music = input('Quer add mais songs?').strip()
    music.append(add_music)
    continuar = input("Quer mais !sr?").strip()
print(music)
    

resposta = resposta.strip()

print(resposta)


idade = input("Pablo, qual a sua idade")

idade = idade.strip()
if idade.isnumeric():
    ano_que_vem  = int(idade) + 1
    ano_que_que_vem = int(idade) + 2
    print(
        f"minha idade ano que vem será..... hehehe {ano_que_vem} "
        f"e ano que que vem... {ano_que_que_vem} "
        "por quê separado se escreve junto e tudo junto se escreve separado?"
    )

else:
    print("errou feio, errou rude")