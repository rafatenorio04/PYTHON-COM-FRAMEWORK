# Peça o valor de um produto e:
produto =  float(input('Digite o valor do produto: '))


# Calcule um desconto de 10%.


desconto = produto * 0.10


# Mostre o valor final.


valor_prod = produto - desconto
print('Valor do produto R$', valor_prod)


# Verifique se o valor final é maior que 100.


print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)


# Verifique se o produto ficou barato (menor que 50).


print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)