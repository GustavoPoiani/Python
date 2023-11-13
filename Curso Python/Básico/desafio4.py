# Soma e média de uma sequencia de numeros
# maior valor da sequencia de numeros

valores=[10,30,-8,0,-2,4]

soma=0
maior=0
for valor in valores:
    soma=soma+valor
    if valor>maior:
        maior=valor

media=soma/len(valores)
print(f"A soma dos valores {valores} é: {soma}")
print(f"A média dos valores {valores} é: {media}")
print(f"O maior valor dos valores {valores} é: {maior}")
print(sum(valores))
print(max(valores))
print("/n")

#palavras com pelo menos 5 caracteres devem ser listadas

palavras=['oi','Python','Programação','xxx']

for palavra in palavras:
    if len(palavra)>=5:
        print(f"A palavra {palavra} possui 5 ou mais caracteres.")
