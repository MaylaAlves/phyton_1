import random

roll = 0
count = 0

print ('A primeira pessoa a obter 5 vitórias!!')
while roll != 5:
    name = input ('Digite um nome, ou \'q\' para sair: ')
    
    if name.strip()=='':
        continue
    
    if name.strip =='q':
        break

    count = count +1
    roll = random.randint(1,5)
    print(f'{name} jogou  {roll} vezes')
else:
    print(f'{name} Campeã(o)!!!')

print(f'Você jogou os dados {count} vezes.')