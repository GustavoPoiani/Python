# Desafio da senha
usuarioC="Gustavo"
senhaC="dunGeon01"

usuario=input("Digite o nome de usuário: ")
senha=input("Digite a senha de acesso: ")

testeUsuario=usuario==usuarioC
testeSenha=senha==senhaC

if testeUsuario and testeSenha:
    print(f"Olá {usuario}, seja bem vindo ao sistema!")
elif testeUsuario and not testeSenha:
    print(f"{usuario}, sua senha está incorreta!")
else:
    print(f"O usuário {usuario}, não foi encontrado no sistema!")


