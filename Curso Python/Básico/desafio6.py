# Criar um código q conta o numero de vogais de um bloco de texto qualquer.
# O código deve desconsiderar letas maiusculas e minusculas, isto é, "a" e "A" contam da mesma forma.

texto="Eu sou o máximo, eu sou o melhor, i am the best!"

vogais={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0}

for letra in texto:
    if letra.lower() == 'a':
        vogais['a']+=1
    if letra.lower() == 'e':
        vogais['e']+=1
    if letra.lower() == 'i':
        vogais['i']+=1
    if letra.lower() == 'o':
        vogais['o']+=1
    if letra.lower() == 'u':
        vogais['u']+=1

for vogal,cont in vogais.items():
    print(f'Há {cont} letras {vogal} no texto.')


