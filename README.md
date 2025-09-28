# Deduplicate Unordered Rows

![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Deduplicate-Unordered-Rows)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 Every Other Day Excel and Power Query Challenges No302 🌟
- 🌟 **Author**: Omid Motamedisedeh

    - In the question table, remove duplicate rows based on the values in columns Value 1 to Value 3, ignoring the order of the values within each row. 
    
    - Example: Rows 1 and 2 are considered duplicates because they contain the same items (A, A, B) regardless of order, so one should be removed.

 🔰 Este script elimina filas duplicadas en un DataFrame de pandas, **ignorando el orden de los valores** en columnas específicas.

 🔗 Link to Excel file:
 👉 https://lnkd.in/grud7rfc

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Deduplicate-Unordered-Rows/blob/main/deduplicate_unordered_rows.py

---
---

## 🧠 Deduplicate Unordered Rows

Este script elimina filas duplicadas en un DataFrame de pandas, **ignorando el orden de los valores** en columnas específicas. Ideal para limpieza de datos donde el contenido es equivalente pero el orden varía.


## 📦 Requisitos

- Python 3.9+
- Paquetes:
- pandas openpyxl (para leer .xlsx)
- tabulate (solo para impresión bonita)
- Archivo Excel con al menos:
    - Las columnas: `ID`, `Value 1`, `Value 2`, `Value 3`.
    - Desde la columna 7 en adelante: resultados esperados para comparación

---

## 🚀 Cómo funciona

1. Carga datos desde Excel (`Sheet1`)
2. Extrae columnas `ID`, `Value1`, `Value2`, `Value3`
3. Crea una columna auxiliar con los valores ordenados como conjunto
4. Elimina duplicados basados en esa columna
5. Imprime el DataFrame limpio

---

## 📤 Salida

El script imprime un DataFrame con:

- `ID`, `Value1`, `Value2`, `Value3`
- Columnas esperadas desde el Excel
- Columnas `Match` con valores `True` o `False`

---

## 🧹 Output:

|ID|Value 1|Value 2|Value 3|ID|Value 1|Value 2|Value 3|Match|
|-|-|-|-|-|-|-|-|-|
|1|A|B|A|1|A|B|A|True|
|3|A|A|A|3|A|A|A|True|
|4|A|C|C|4|A|C|C|True|
|5|A|C|A|5|A|C|A|True|
|6|A|B|C|6|A|B|C|True|
|9|C|C|C|9|C|C|C|True|

---

## 🛠️ Personalización

Puedes adaptar el script para:

- Aplicar reglas más complejas
- Exportar el resultado a Excel o CSV

---

## 🚀 Ejecución

import pandas as pd
from tabulate import tabulate
## 🧩 Componentes
```python
df_raw = pd.read_excel(url, header=1)
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, 1:5]
```

## 🧠 Funcion para comparar el resultado con el Data Frame dado.
```python
def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    comparison = df_actual.eq(df_expected.reset_index(drop=True)).all(axis=1)
    return pd.concat([df_actual, df_expected, comparison.rename('Match')], axis=1)
```

## 🎯 Crear columna auxiliar con los valores ordenados como conjunto
```python
df_input['SortedValues'] = df_input[['Value 1', 'Value 2', 'Value 3']].apply(lambda row: tuple(sorted(row)), axis=1)
```

## 🧹 Eliminar duplicados basados en esa columna
```python
df_unique = df_input.drop_duplicates(subset='SortedValues').drop(columns='SortedValues')
df_unique = df_unique.reset_index(drop=True)
```

## 🧪 Comparación con columnas esperadas
```python
test = df_raw.iloc[:, 6:].copy().dropna(how='all', axis=0)
df_final = compare_with_expected(df_unique, test)
```

## 📊 Visualización
```python
print(tabulate(df_final.values, headers=df_final.columns, tablefmt='fancy'))
```
---
## 📄 Licencia
---
Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.
