resposta = input("Pablo, qual é a musica?")
resposta = resposta.strip()
print(resposta)


idade = input("Pablo, qual a sua idade")

idade = idade.strip()
if idade.isnumeric():
    ano_que_vem  = int(idade)+1
    print("minha idade ano que vem será..... hehehe ",ano_que_vem)

else:
    print("errou feio, errou rude")

