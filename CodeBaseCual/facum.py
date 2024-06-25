def calcular_frecuencia_a(fr):
    
    frec_ac = []
    suma_frecuencias = 0
    for elemento in fr:
        suma_frecuencias += elemento
        frec_ac.append(suma_frecuencias)
    
    return frec_ac