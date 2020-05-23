produtos = {
    1: {'nome':'cookie de mandolate', 'peso':50, 'estoque':152, 'preço':20.},
    2: {'nome':'cookie de cerveja', 'peso':50, 'estoque':20, 'preço':40.}, 
    3: {'nome':'cookie feio mas gostoso', 'peso':50, 'estoque':25, 'preço':45},
    4: {'nome':'rocambole de cookie', 'peso':50, 'estoque':12319239128391283, 'preço':34},
}

clientes = [
    {'nome':'pythrick'},
    {'nome':'RochaCBruno'},
    {'nome':'luiz'},
]

pedidos = []

pedidos.append({'numero':1000, 'itens':[{'produto':2, 'qtd':3}], 'cliente':'pythrick'})
pedidos.append({'numero':1001, 'itens':[{'produto':4, 'qtd':1}], 'cliente':'RochaCBruno'})
pedidos.append({'numero':1002, 'itens':[{'produto':1, 'qtd':2}, {'produto':4, 'qtd':14}], 'cliente':'luiz'})

# calcular peso e preço
for pedido in pedidos:
    nome_do_cliente = pedido['cliente']
    peso_total = 0
    preço_total = 0
    for item in pedido['itens']:
       id_do_produto = item['produto']
       quantidade_do_produto = item['qtd']
       produto = produtos[id_do_produto]
       peso_individual = quantidade_do_produto * produto['peso']
       preço_individual = quantidade_do_produto * produto['preço']
       preço_total += preço_individual
       peso_total += peso_individual
    print(f'Cliente: {nome_do_cliente} - O peso do pedido é {peso_total}, e o preço do pedido é {preço_total} impeachments :)')
                