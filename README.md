
# Eficiencia Computacional de QuickSort y Tablas Hash con Encadenamiento Separado ante el Aumento del Tamaños de Datos

**Descripción:**  
Proyecto de análisis de rendimiento para la estructura de datos **Tabla Hash con encadenamiento separado** en Python y el algoritmo de ordenamiento **QuickSort**. 

**Hash:**
Este repositorio contiene una implementación simple de tabla hash (array de cubetas con listas enlazadas para colisiones) y un sistema de pruebas automatizadas para medir su eficiencia. Se incluyen funciones para medir el **tiempo de inserción, búsqueda y borrado** de claves, así como el **uso de memoria** durante la inserción. Los resultados de las pruebas se exportan a archivos CSV, y se proporcionan scripts para visualizar estos resultados. El proyecto es útil tanto para desarrolladores interesados en el comportamiento práctico de las hash tables, como para fines académicos al analizar la complejidad empírica y uso de recursos.

**QuickSort:**
Este repositorio contiene el código y los recursos para el análisis empírico de la eficiencia computacional del algoritmo de ordenamiento QuickSort. El estudio evalúa el rendimiento de QuickSort en términos de tiempo de ejecución y uso de memoria (RAM) frente a la variación del tamaño de los datos y diferentes escenarios de entrada (caso promedio, peor caso y casos con duplicados).

## Clonación del repositorio

```bash
git clone https://github.com/AliciaEA/InvAlgEstDatos_Qck_Hsh.git
cd analisis-hash
```

## Configuración del entorno y dependencias

Se recomienda utilizar un **entorno virtual de Python**. Asegúrese de tener **Python 3.10+**.

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

# Instalación de dependencias
pip install memory_profiler pandas matplotlib
```

## Uso del programa HASH

Ejecute:

```bash
python main.py
```

### Opciones

1. **Prueba personalizada:** Exporta `personalizada_hash.csv`.  
2. **Perfil de memoria:** Exporta `memoria_hash.csv`.  
3. **Experimento completo:** Exporta `resultados_hash.csv`.  
4. **Salir**

### Análisis de resultados

Use los scripts:

```bash
python memoria_hash.py
python resultados_hash.py
```

Para graficar: uso de memoria vs número de elementos, o comparativas de tiempo.

### Archivos generados

- `personalizada_hash.csv`: Una sola prueba
- `memoria_hash.csv`: Medición de uso de memoria
- `resultados_hash.csv`: Experimento completo con promedios y desviaciones estándar

## Uso del programa QUICKSORT
* Implementa QuickSort con pivote central.
* Genera listas de datos para pruebas.
* Mide el tiempo de ejecución (en segundos).
* Mide el pico de uso de memoria (en MiB).
* Muestra resultados en tablas y gráficos logarítmicos.

### 🛠️ Tecnologías Usadas

* `pandas` (para tablas)
* `matplotlib` (para gráficos)
* `memory_profiler` (para medir memoria)

### 🚀 Cómo Ejecutar

1.  **Instala las dependencias:**
    ```bash
    pip install pandas matplotlib memory_profiles
    ```
2.  **Ejecuta el script principal:**
    ```bash
    python main.py
    ```
    Los resultados se mostrarán en la consola y se abrirán ventanas con los gráficos.

### 📁 Estructura del Código

* `quicksort_algo.py`: La lógica del algoritmo QuickSort.
* `data_generator.py`: Crea los diferentes tipos de listas para probar.
* `performance_metrics.py`: Contiene funciones para medir el tiempo. Procesa y formatea los resultados en tablas.
* `plotter.py`: Genera los gráficos de rendimiento.
* `main.py`: Coordina todo el proceso de análisis.

## Créditos

Desarrollado por *David Sánchez, Andrea Duarte, Franco Aguilera, Sara Zambrana, Alicia Estrada*  
Clase: *Algoritmos y estructuras de datos*  
Año: 2025  

