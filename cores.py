cores = ['vermelho', 'fucshia', 'verde', 'roxo']
print(cores[1])


foods = ['abacate', 'pipoca', 'sorvete']
print(f"Bruno, pufavo pega {foods[1][:3]}")

print(f"Bruno, pufavo pega o {foods[0]} {cores[0]}")

foods.append('caqui')
foods.append('guacamole')
print(foods)
foods.insert(-2,'kiwi')
print(foods)

onde_ta = foods.index('pipoca')
foods.insert(onde_ta + 1,'arroz')
print(foods)

drinks = ['mojito', 'cerveja', 'champagne', 'bombeirinho']
foods.extend(drinks)
print(foods)

print(sorted(foods))

for food in sorted(foods):
    print(food)

continuar = 'sim'
while continuar == 'sim':
    add_food = input('O Bruno quer saber qual foods vc quer')
    foods.append(add_food)
    continuar = input('Ainda quer mais foods?')
print("ta bom então ta bom ")
print(f"sua lista de foods é...{foods}")    

