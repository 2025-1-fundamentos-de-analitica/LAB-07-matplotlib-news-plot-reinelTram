"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    # Configurar rutas
    input_path = os.path.join("files", "input", "news.csv")  
    output_dir = os.path.join("files", "plots")              
    os.makedirs(output_dir, exist_ok=True)                 

    # Leer datos
    try:
        df = pd.read_csv(input_path, index_col=0)  
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo en {input_path}. Verifica la ruta.")

    # Configurar estilos
    styles = {
        'Television': {'color': 'dimgray', 'linewidth': 1, 'zorder': 1},
        'Newspaper': {'color': 'gray', 'linewidth': 1, 'zorder': 1},
        'Radio': {'color': 'lightgray', 'linewidth': 1, 'zorder': 1},
        'Internet': {'color': 'tab:blue', 'linewidth': 4, 'zorder': 2}
    }

    #  Crear figura
    plt.figure(figsize=(10, 6))

    # Dibujar líneas y puntos
    first_year = df.index[0]
    last_year = df.index[-1]

    for column in df.columns:
       
        plt.plot(
            df.index,
            df[column],
            color=styles[column]['color'],
            linewidth=styles[column]['linewidth'],
            zorder=styles[column]['zorder']
        )
        
        # Puntos y etiquetas
        plt.scatter(
            [first_year, last_year],
            [df[column].iloc[0], df[column].iloc[-1]],
            color=styles[column]['color'],
            s=30,
            zorder=3
        )
        
        # Etiqueta inicial 
        plt.text(
            first_year - 0.3,
            df[column].iloc[0],
            f"{column} {df[column].iloc[0]}%",
            ha='right',
            va='center',
            color=styles[column]['color'],
            fontsize=9,
            zorder=4
        )
        
        # Etiqueta final 
        plt.text(
            last_year + 0.3,
            df[column].iloc[-1],
            f"{df[column].iloc[-1]}%",
            ha='left',
            va='center',
            color=styles[column]['color'],
            fontsize=9,
            zorder=4
        )

    #  Personalizar ejes y estilo
    plt.title("People Get News From... (2001-2010)", fontsize=16, pad=20)
    plt.xticks(df.index, df.index.astype(str), ha='center')
    
    for spine in ['top', 'right', 'left']:
        plt.gca().spines[spine].set_visible(False)
    plt.gca().yaxis.set_visible(False)

    #  Guardar 
    output_path = os.path.join(output_dir, "news.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    return f"{output_path}"


if __name__ == "__main__":
    print(pregunta_01())