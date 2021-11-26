#Lidando com um Baralho de cartas

import random

nipes = ["Copas", "Espadas","Ouros", "Paus" ]
classes = ["2", "3", "4", "5", "6","7","8","9","10","Valete","Rei","Rainha", "A's"]
baralho = []

for nipe in nipes:
    for classe in classes:
        baralho.append(f'{classe} de {nipe}')

print(f'Há {len(baralho)} cartas no baralho.')

print('Distribuindo...')

mao = []

while len(mao) < 5:
    carta = random.choice(baralho)
    baralho.remove(carta)
    mao.append(carta)

print(f'Há {len(baralho)} cartas no baralho.')
print('O jogador tem as seguintes cartas em sua mão:')
print(mao)