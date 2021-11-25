import random

valor = random.randint(1,10)
contador = 0
chute = 0
print('Chute um numero entre 1 e 10')

while chute != valor:
    contador+=1
    chute = input (f'Entre com um chute #{contador}: ')
    if chute.isnumeric():
        chute = int(chute)
    else:
        print('Somente números, por favor!')
        continue

    if chute > valor:
        print('Você chutou um número muito alto, tente novamente!')
    elif chute < valor:
        print ('Você chutou um número muito baixo, por favor tente novamente!')
    
else:
    print(f'Você chutou {contador} vezes!')
