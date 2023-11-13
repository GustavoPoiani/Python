# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

estados_e_capitais = {
    "São Paulo": "São Paulo",
    "Rio de Janeiro": "Rio de Janeiro",
    "Ceará": "Fortaleza",
    "Mato Grosso": "Cuiabá",
    "Minas Gerais": "Belo Horizonte",
    "Rio Grande do Sul": "Porto Alegre",
    "Amazonas": "Manaus",
    "Paraná": "Curitiba",
    "Pará": "Belém",
    # ... Preencha com todos os estados aqui!
}

quer_continuar = True
rodadas=0
acertos=0

for estado, capital in estados_e_capitais.items():
    if not quer_continuar:
        break
    rodadas+=1
    print(f"--> Qual a capital do estado {estado}?")
    resposta = input("Sua resposta: ")
    if resposta.lower() == capital.lower():
        print("Resposta correta!")
        acertos+=1
    else:
        print(f"Resposta errada! O correto seria {capital}")
    while True:
        opcao = input("Deseja continuar? (s/n): ").lower()
        if opcao not in ["s", "n"]:
            print('Responda apenas com "s" para sim ou "n" para não.')
            continue
        elif opcao == "n":
            quer_continuar = False
        break

porc=(acertos/rodadas)*100

print('----------------------------------------')
print(f'Você acertou {acertos} de {rodadas}.')
print(f'Porcentagem de acertos: {porc:2f}%')
