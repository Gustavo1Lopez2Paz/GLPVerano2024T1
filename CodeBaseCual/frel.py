# Calcular la frecuencia relativa en base a la frecuencia absoluta
def frecuencia_rel(frecuencia_abs):
    fr = []
    tot_fa = sum(i for i in frecuencia_abs)

    # Agregar datos de frecuencia relativa
    for frec in frecuencia_abs:
        frel = (frec * 100) / tot_fa
        fr.append(frel)

    return fr