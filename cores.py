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