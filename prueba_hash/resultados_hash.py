import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('resultados_hash.csv')
# Filtrar por tamaño de tabla, por ejemplo 2000
table_size = 5000
df_filtrado = df[df['table_size'] == table_size]

plt.figure(figsize=(8, 5))
plt.plot(df_filtrado['n_elements'], df_filtrado['memory_usage_avg'], marker='o', label=f'Tabla {table_size}')
plt.xlabel('Número de elementos insertados (n_elements)')
plt.ylabel('Uso promedio de memoria (MB)')
plt.title('Carga de datos vs Uso de memoria\n(resultados_hash.csv, tabla=2000)')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
