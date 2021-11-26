#Testar um valor para inclusão em uma lista

#numeros = [1,3,5]

#print (5 in numeros)
#print (8 in numeros)

#print(5 not in numeros)
#print(8 not in numeros)

#Executar um loop em uma lista

#cidades = ['São José dos Campos', 'Jacareí', 'Caçapava']

#for cidade in cidades:
#    print(cidade)

#Interromper um loop for depois de encontrarmos um valor que exceda um limite específico.

#numeros = [42, 77, 16, 101, 23, 8, 4, 15, 55]
#numeros.sort()

#for numero in numeros:
#    if numero > 42:
#        break
#    print(numero)

#Usar uma instrução else

#import random
#numeros = []

#while len(numeros) < 5:
#    numeros.append(random.randint(1,100))

#for numero in numeros:
#    print(numero)
#    if numero >=90:
#        print('Encontrado pelo menos um número maior que 90')
#        break
#else:
#    print('Nenhum número maior que 90')

#print('Completo!')


#programa que filtra uma lista. A lista contém int e string. Queremos criar uma lista que contenha apenas os valores str. Usamos a instrução continue para ir para o próximo item na lista, em vez de adicionar o item atual à lista filtrada.

#valores = ["computador", 7, "telefone", 3, "camera", 5 ]
#equipamentos = []

#for valor in valores:
#    if isinstance(valor, str)== False:
#        continue
#    equipamentos.append(valor)

#print(equipamentos)

#Criar loops for aninhados

#nipes = ["Copas", "Espadas","Ouros", "Paus" ]
#classes = ["2", "3", "4", "5", "6","7","8","9","10","Valete","Rei","Rainha", "A's"]

#for nipe in nipes:
#    for classe in classes:
#        print(f'{classe} de {nipe}')


#Escolher aleatoriamente em uma lista

import random

numeros = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selecao_numero = random.choice(numeros)
print(selecao_numero)

selecao_numero = random.choices(numeros, k=3)
print(selecao_numero)