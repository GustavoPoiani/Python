# Desafio - crie um programa que:
# - Pede elo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos
nome = input("Qual seu nome:? ")
idade = int(input("Qual sua idade:? "))
print("Oi, " + nome + "!")
letras = str(len(nome))
print("Seu nome tem " + letras + " letras.")
print("Daqui a 5 anos, você terá " + str(idade + 5) + " anos.")
