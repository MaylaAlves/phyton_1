import random

valor = random.randint(1,5)
contador = 0
chute = 0

while chute != valor:
    contador+=1
    chute = input ('Chute um número entre 1 e 5: ')
    if chute.isnumeric():
        chute = int(chute)
else:
    print(f'Você chutou {contador} vezes!')
