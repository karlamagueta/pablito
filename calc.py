# desenvolva uma calculadora que pergunta para o usuario no term 2 numeros e qual op.; quer fazer
# exemplo: Qual o primeiro numero / q   ual segundo / qual op. (as ops serão em texto - sum, mul, sub, div)

add_numero_1 = int(input('Qual o numero que vc deseja add?').strip())
add_numero_2 = int(input('Quak o segundo numero que vc deseja add?').strip())
operação = input('Qual a operação?').strip()

if operação == 'soma':
    total = add_numero_1 + add_numero_2
    
elif operação == 'subtração':
    total = add_numero_1 - add_numero_2   
    
elif operação == 'multiplicação':
    total = add_numero_1 * add_numero_2

elif operação == 'divisão':
    total = add_numero_1 / add_numero_2  

else:
    raise AttributeError('isso não te pertence!')    

print(total)
