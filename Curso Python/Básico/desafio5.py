# Dado duas listas, printe todos os valores que aparecem duplicados nas duas listas
# Dado duas listas, printe uma msg dizendo se existe algum elemento em comun entre elas ou nao.

lista1=[3,4,6]
lista2=[1,2,7,8]
existe=False

for valor1 in lista1:
    for valor2 in lista2:
        if valor1==valor2:
            print(f'O valor {valor1} da lista1 é igual ao valor {valor2} da lista2.')
            existe=True

if existe:
    print('Existe valor em comum entre as duas listas.')
else:
    print('Não existe valor em comum entre as duas listas.')
