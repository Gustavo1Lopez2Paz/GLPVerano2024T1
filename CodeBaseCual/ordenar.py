def format_list(datos):
    lista = []
    for dato in datos:
        palabra = dato.strip().upper()
        lista.append(palabra)
    return lista