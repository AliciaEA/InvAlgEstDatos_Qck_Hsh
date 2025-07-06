import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv('resultados_hash.csv')

# Seleccionar el tamaño de tabla a graficar
table_size = 5000
df_filtrado = df[df['table_size'] == table_size]

# Asegurarse que n_elements es int
df_filtrado['n_elements'] = df_filtrado['n_elements'].astype(int)

plt.figure(figsize=(12, 8))

# Graficar la curva con marcadores
plt.plot(
    df_filtrado['n_elements'],
    df_filtrado['memory_usage_avg'],
    marker='o',
    label=f'Tabla {table_size}'
)

# Graficar la curva de tiempo de inserción
plt.plot(
    df_filtrado['n_elements'],
    df_filtrado['insert_time_avg'],
    marker='o',
    label=f'Tabla {table_size}'
)
plt.ylabel('Tiempo promedio de inserción (s)')

# Etiquetas de los ejes y título
plt.xlabel('Número de elementos insertados (n_elements)')
plt.ylabel('Uso promedio de memoria (MB)')
plt.title(f'Carga de datos vs Uso de memoria\n(resultados_hash.csv, tabla={table_size})')
plt.grid(True)
plt.tight_layout()
plt.legend()

# Mostrar solo los valores exactos de n_elements como ticks del eje X
plt.xticks(
    df_filtrado['n_elements'],
    [f"{n:,}" for n in df_filtrado['n_elements']],  # Muestra 20,000 en vez de 20000
    rotation=45
)

# Agregar etiquetas encima de cada punto con el valor de memoria (opcional, pero profesional)
for x, y in zip(df_filtrado['n_elements'], df_filtrado['memory_usage_avg']):
    plt.annotate(
        f"{y:.1f}",
        (x, y),
        textcoords="offset points",
        xytext=(0,8),
        ha='center',
        fontsize=9,
        color='navy'
    )
# Y etiquetas encima del punto:
for x, y in zip(df_filtrado['n_elements'], df_filtrado['insert_time_avg']):
    plt.annotate(
        f"{y:.4f}",
        (x, y),
        textcoords="offset points",
        xytext=(0,8),
        ha='center',
        fontsize=9,
        color='darkgreen'
    )

plt.show()
