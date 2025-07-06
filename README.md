
# Análisis de rendimiento de Tablas Hash (Encadenamiento Separado)

**Descripción:**  
Proyecto de análisis de rendimiento para la estructura de datos **Tabla Hash con encadenamiento separado** en Python. Este repositorio contiene una implementación simple de tabla hash (array de cubetas con listas enlazadas para colisiones) y un sistema de pruebas automatizadas para medir su eficiencia. Se incluyen funciones para medir el **tiempo de inserción, búsqueda y borrado** de claves, así como el **uso de memoria** durante la inserción. Los resultados de las pruebas se exportan a archivos CSV, y se proporcionan scripts para visualizar estos resultados. El proyecto es útil tanto para desarrolladores interesados en el comportamiento práctico de las hash tables, como para fines académicos al analizar la complejidad empírica y uso de recursos.

## Clonación del repositorio

```bash
git clone <URL-del-repositorio.git>
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

## Uso del programa

Ejecute:

```bash
python main.py
```

### Opciones:

1. **Prueba personalizada:** Exporta `personalizada_hash.csv`.  
2. **Perfil de memoria:** Exporta `memoria_hash.csv`.  
3. **Experimento completo:** Exporta `resultados_hash.csv`.  
4. **Salir**

## Análisis de resultados

Use los scripts:

```bash
python memoria_hash.py
python resultados_hash.py
```

Para graficar: uso de memoria vs número de elementos, o comparativas de tiempo.

## Archivos generados

- `personalizada_hash.csv`: Una sola prueba
- `memoria_hash.csv`: Medición de uso de memoria
- `resultados_hash.csv`: Experimento completo con promedios y desviaciones estándar

## Créditos

Desarrollado por *David Sánchez, Andrea Duarte, Franco Aguilera, Sara Zambrana, Alicia Estrada *  
Clase: *Algoritmos y estructuras de datos*  
Año: 2025  
