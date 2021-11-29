#criar e chamar uma função pequena

#def diga_ola():
#    print('Olá Mundo!!!')

#diga_ola()

#add código que aceita um parâmetro de entrada

#def diga_ola(nome):
#    print(f'Olá {nome}!!!')

#diga_ola('Laura')

#Modificar a chamada de função para remover o argumento

#def diga_ola(nome='Mundo'):
#    print(f'Olá {nome}!!!!')

#diga_ola()
#diga_ola('Laura')

#incluindo um segundo parâmetro de entrada opcional
#def diga_ola (nome='Mundo', saudacoes=None):
#    if saudacoes == None:
#        print(f'Olá {nome}!')
#    else:
#        print(f'{saudacoes} {nome}')

#diga_ola()
#diga_ola('Laura')
#diga_ola(saudacoes ='Oi')
#diga_ola('Laura', 'Oi')

#função que retorna um valor usando a palavra-chave return.

#def add_dois_numeros (x,y):
#    return x + y

#add_dois_numeros (4, 6)
#resultado = add_dois_numeros (5, 7)
#print (resultado)

#função que retorna uma lista

def criando_baralho():
    nipes = ["Ouro", "Espadas", "Paus", "Copas"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "A's"]
    baralho = []

    for nipe in nipes:
        for rank in ranks:
            baralho.append(f'{rank} of {nipe}')
    
    return baralho

meu_baralho = criando_baralho()
print(len(meu_baralho))





