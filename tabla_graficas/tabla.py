import pandas as pd
def tabla_grouped(lim_inf, lim_sup, mrks, freq_absoluta, freq_relativa, frecuencia_acumulada):
   
    # Create the DataFrame with column headers
    data = {'Limite inferior': lim_inf,
            'Limite superior': lim_sup,
            'Marcas de clase': mrks,
            'Frecuencia absoluta': freq_absoluta,
            'Frecuencia Relativa': freq_relativa,
            'Frecuencia Acumulada': frecuencia_acumulada}
    
    df = pd.DataFrame(data)
    return df

def imptabla(clases_sorted, fa_sorted, fr_relativa, fr_acum):

    # Create the DataFrame with column headers
    data = {'Clases': clases_sorted,
            'F absoluta': fa_sorted,
            'F relativa': fr_relativa,
            'F acumulada': fr_acum}
    
    df = pd.DataFrame(data)
    return df
    