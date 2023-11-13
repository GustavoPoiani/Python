# Desafio 3 - acerte o numero

nSecreto = 10
descobriu = False

if not descobriu:
    palpite = int(input("Descubra o número!\nSeu palpite: "))
    if palpite < nSecreto:
        print("Palpite muito baixo!")
    elif palpite > nSecreto:
        print("Palpite muito alto!")
    else:
        print("Você descobriu!")
        descobriu = True
if not descobriu:
    palpite = int(input("Descubra o número!\nSeu palpite: "))
    if palpite < nSecreto:
        print("Palpite muito baixo!")
    elif palpite > nSecreto:
        print("Palpite muito alto!")
    else:
        print("Você descobriu!")
        descobriu = True
if not descobriu:
    palpite = int(input("Descubra o número!\nSeu palpite: "))
    if palpite < nSecreto:
        print("Palpite muito baixo!")
    elif palpite > nSecreto:
        print("Palpite muito alto!")
    else:
        print("Você descobriu!")
        descobriu = True
if descobriu:
    print("Parabéns! Você ganhou!")
else:
    print(f"Você perdeu! O número secreto era {nSecreto}!")
