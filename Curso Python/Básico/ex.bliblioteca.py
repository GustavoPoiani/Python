# Exemplos de biblioteca
import math
import datetime
import random
import os
import time

print(math.pi)
print(math.log(16,2))
print('--------------------')

agora=datetime.datetime.now()
ano_2000=datetime.datetime(2000,1,1)
print(agora-ano_2000)
print('--------------------')

for _ in range(5):
    n=random.randint(1,10)
    print(f'Número escolhido: {n}')
print('--------------------')

nomes=['Juliano','Marcos','Paulo']
for _ in range(5):
    nome=random.choice(nomes)
    print(f'Nome escolhido: {nome}')
print('--------------------')

print(os.getcwd())
print(os.listdir())
print('--------------------')

inicio=time.time()
print('Primeira linha')
time.sleep(1)
print('Segunda linha')
final=time.time()
tempo_execucao=final-inicio
print(f'O script levou {tempo_execucao:.7f} segundos para executar.')

