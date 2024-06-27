import matplotlib.pyplot as plt
# Histograma
def plot_hist(clases, freq_absoluta, mrks, labelx, labely, titulo):
    plt.figure(figsize=(12, 8))  # Set the figure size

    # Ajustar el ancho de las barras según el tamaño de los datos
    if max(mrks) > 500:
        bar_width = 30.0
    else:
        bar_width = 0.3

    plt.bar(mrks, freq_absoluta,
           width=bar_width, edgecolor="k",
           color=["#14BF48", "#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#33FFBE"])
    
    plt.xticks(mrks,  fontsize=12)
    plt.xlabel(labelx, fontsize=15)  # X-axis label
    plt.ylabel(labely, fontsize=15)  # Y-axis label
    plt.title(titulo, fontsize=20)  # Title
    plt.grid()  # Enable grid
    plt.show()  # Display the plot
    
"""def plot_hist(clases, freq_absoluta, mrks, labelx, labely, titulo):

    plt.figure(figsize=(12, 8))  # Set the figure size

    plt.bar(mrks, freq_absoluta,
           width=0.3, edgecolor="k",
           color=["#14BF48", "#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#33FFBE"])
    
    plt.xticks(mrks,  fontsize=12)
    plt.xlabel(labelx, fontsize=15)  # X-axis label
    plt.ylabel(labely, fontsize=15)  # Y-axis label
    plt.title(titulo, fontsize=20)  # Title
    plt.grid()  # Enable grid
    plt.show()  # Display the plot"""

# Poligono de frecuencia
def plot_poligono(clases, fa_sorted,marcas_texto, labelx, labely, titulo):
# Datos
    plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico


    # Ajustes para el graficado del polígono
    datos_x = [0] + clases + [len(clases) + 1]
    datos_y = [0] + fa_sorted + [0]

    plt.plot(datos_x, datos_y, 
        linewidth=5, color="g", linestyle="--", 
        marker="v", markersize=10, markerfacecolor="y", markeredgecolor="r")

    plt.xticks(clases, marcas_texto, fontsize=12, rotation=45)
    plt.xlabel(labelx, fontsize=15)  # Etiqueta del eje x
    plt.ylabel(labely, fontsize=15)  # Etiqueta del eje y
    plt.title(titulo, fontsize=20)  # Etiqueta del título
    plt.grid()  # Activar cuadrícula
    plt.show()  # Mostrar gráfico

# Diagrama de barras
def plot_barras(clases, fa_sorted,marcas_texto, labelx, labely, titulo):

        plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico

        # marcas_clase = [0.165, 0.495, 0.825, 1.155, 1.485]  # Datos del eje x
        # frecuencias = [6, 4, 3, 3, 4]  # Datos del eje y
        # marcas_texto = ["0.165", "0.495", "0.825", "1.155", "1.485"]

        plt.barh(clases, fa_sorted,
                height=0.5, edgecolor="k",
                color=["#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#333CFF", "#33FFBE"])

        plt.yticks(clases, marcas_texto, fontsize=12, rotation=45)
        plt.xlabel(labelx, fontsize=15)  # Etiqueta del eje x
        plt.ylabel(labely, fontsize=15)  # Etiqueta del eje y
        plt.title(titulo, fontsize=20)  # Etiqueta del título
        plt.grid()  # Activar cuadrícula
        plt.show()  # Mostrar gráfico

# Ojiva
def plot_ojiva(clases, fr_acum, marcas_texto, labelx, labely, titulo):
    plt.figure(figsize=(12, 6))  # Ancho, Alto del gráfico

    # Ajustes para el graficado del polígono
    datos_x = [0] + clases 
    datos_y = [0] + fr_acum 

    plt.plot(datos_x, datos_y, 
            linewidth=5, color="g", linestyle="--", 
            marker="v", markersize=10, markerfacecolor="y", markeredgecolor="r")

    plt.xticks(clases, marcas_texto, fontsize=15, rotation=0)
    plt.xlabel(labelx, fontsize=25)  # Etiqueta del eje x
    plt.ylabel(labely, fontsize=25)  # Etiqueta del eje y
    plt.title(titulo, fontsize=40)  # Etiqueta del título
    plt.grid()  # Activar cuadrícula
    plt.show()  # Mostrar gráfico

# Diagrama de pastel
def plot_pie(fr_relativa, marcas_texto, titulo):
    plt.figure(figsize=(8, 8))
    plt.pie(fr_relativa,
            autopct="%0.1f%%",
            colors=["#14BF48", "#33FFBE", "#333CFF", "#FF3349", "#F6FF33", "#33FFBE"],
            labels=marcas_texto)
    plt.title(titulo, fontsize=20)
    plt.show()