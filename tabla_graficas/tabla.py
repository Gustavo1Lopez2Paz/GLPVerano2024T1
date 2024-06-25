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
    