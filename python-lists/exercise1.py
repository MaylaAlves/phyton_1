#criando uma lista de valores

cores = ['vermelho', 'verde', 'azul', 'amarelo', 'laranja', 'roxo', 'marrom']

#print(cores)
#print (type(cores))

#add uma cadeia de caracteres, float, inteiro e valor booliano a uma lista.

#sortido = ['Laura', 3.14, 7, False]
#print(sortido)
#print (type(sortido))

#lista vazia
#minha_lista = []

#Usando um índice para acessar elementos individuais

#print (f'Indexação baseada em 0 na lista ... segundo item: {cores[1]}')
#print(f'Último item da lista: {cores[-1]}')
#print(f'Próximo ao último item da lista: {cores[-2]}')

#criando fatias

#print ('\nImprima uma fatia começando no índice 2 e excluindo o índice 5: ')
#print(cores[2:5])
#print (type(cores[2:5]))

#print ('\nImprima uma fatia começando no índice 0 ao índice 3: ')
#print(cores[:3])

#print ('\nImprima uma fatia começando no índice 4 para o índice final da lista: ')
#print(cores[4:])

#print ('\nImprima uma fatia começando do 4º ao final (mas não o último item): ')
#print(cores[-4:-1])

#Reverter e classificar a lista

#cores.reverse()
#print(cores)

#cores.sort()
#print(cores)

#Tratar a lista como uma fila
#print(cores)

#cor = cores.pop(0)
#print('popped', cor)

#print(cores)

#Adicionar e remover elementos de uma lista

#print(cores)
#cores.append ('preto')
#cores.append ('branco')

#cores.remove ('amarelo')
#cores.remove ('laranja')

#print(cores)

#Combinar uma nova lista com uma lista existente

#novas_cores = ['pink', 'cinza']
#cores.extend(novas_cores)
#print(cores)

#Limpar todos os itens de uma lista

print(cores)
cores.clear()
print(cores)