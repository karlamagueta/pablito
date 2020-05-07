resposta = input("Pablo, qual é a musica?")
print(resposta)

# input
idade = input("Pablo, qual a sua idade")

# validacao
idade = idade.strip()
if not idade.isnumeric():
    print("errou feio, errou rude")
else:
    # computacao / processamento
    ano_que_vem = int(idade) + 1

    # output
    print("minha idade ano que bem é", ano_que_vem)
