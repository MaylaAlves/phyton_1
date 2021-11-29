def process_numeros(lista_naoprocessada):
    lista_processada = []
    if isinstance (lista_naoprocessada, list) == False:
        return lista_processada

    for item in lista_naoprocessada:
        if isinstance(item, int):
            lista_processada.append(item)
        elif isinstance (item, str):
            if item.isnumeric():
                converted_item = int(item)
                lista_processada.append (converted_item)
    
    lista_processada.sort()
    return lista_processada

def process_nomes(lista_naoprocessada):
    lista_processada = []
    if isinstance (lista_naoprocessada, list) == False:
        return lista_processada

    for item in lista_naoprocessada:
        if isinstance (item, str):
            if item.isnumeric() == False:
                lista_processada.append (item)
    
    lista_processada.sort()
    return lista_processada