def ordenar_asc(arreglo):

    fa_sorted = []    

    arr_len =len(arreglo)
    
    for i in range(arr_len):                
        min_idx = i
        for j in range(i + 1, arr_len):
            if arreglo [j] < arreglo[min_idx]:
                min_idx = j
    
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
        
    return(arreglo)