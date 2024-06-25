def obtener_fa(fr):
    
    fa = []
    suma = 0
    
    for elemento in fr:
        
        suma += elemento
        fa.append(suma)
        
    return fa