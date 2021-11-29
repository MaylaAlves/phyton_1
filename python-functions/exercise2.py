#Add listas de argumentos arbitrários e argumentos de palavra-chave a funções

#def print_args (*args):
#    for arg in args:
#        print(f'arg = {arg}')

#print_args ('a')
#print_args ('a', 'b')
#print_args ('a', 'b', 'c')

#adicionar código que aceita argumentos de palavra-chave

def print_keyword_args (**kwargs):

    print ('\n')
    print (kwargs)
    print (type(kwargs))

    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')

    terceiro = kwargs.get('terceiro', None)
    if terceiro != None:
        print ('Terceiro argumento = ', terceiro)
    
print_keyword_args(primeiro = 'a')
print_keyword_args (primeiro = 'b', segundo = 'c')
print_keyword_args (primeiro = 'd', segundo ='e', terceiro = 'f')