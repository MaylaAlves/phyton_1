#Preenchendo funções ausentes

import processor

minha_lista = [5, 'Dan', '4', 7, 'Steve', 'Amy', 'Rhonda', 4, '9', 'Jill', 7, 'Kim']
minha_lista_ruim = 5

numeros = processor.process_numeros(minha_lista)
print(numeros)

nomes = processor.process_nomes(minha_lista)
print(nomes)

numeros = processor.process_numeros(minha_lista_ruim)
print(numeros)

nomes = processor.process_nomes(minha_lista_ruim)
print(nomes)