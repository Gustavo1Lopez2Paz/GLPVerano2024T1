import math

def clases_grouped(datos):
    amplitud = round(max(datos) - min(datos), 2)
    nclases = 1 + (3.3*math.log10(len(datos)))
    anc_clas = round(amplitud / math.floor(nclases), 2)

    marc_clase = []
    lim_inf = []
    lim_sup = []

    for i in range(int(nclases)):
        marc_clase.append(round(min(datos) + i*anc_clas + anc_clas/2, 3))
        lim_inf.append(round(min(datos) + i*anc_clas, 2))
        lim_sup.append(round(min(datos) + (i+1)*anc_clas, 2))

    return lim_inf, lim_sup, marc_clase