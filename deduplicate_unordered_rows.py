import pandas as pd
from tabulate import tabulate
df_raw = pd.read_excel(url, header=1)
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, 1:5]


# Funcion para comparar el resultado con el Data Frame dado.
def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    comparison = df_actual.eq(df_expected.reset_index(drop=True)).all(axis=1)
    return pd.concat([df_actual, df_expected, comparison.rename('Match')], axis=1)


# Crear columna auxiliar con los valores ordenados como conjunto
df_input['SortedValues'] = df_input[['Value 1', 'Value 2', 'Value 3']].apply(lambda row: tuple(sorted(row)), axis=1)

# Eliminar duplicados basados en esa columna
df_unique = df_input.drop_duplicates(subset='SortedValues').drop(columns='SortedValues')
df_unique = df_unique.reset_index(drop=True)

test = df_raw.iloc[:, 6:].copy().dropna(how='all', axis=0)
df_final = compare_with_expected(df_unique, test)
print(tabulate(df_final.values, headers=df_final.columns, tablefmt='fancy'))
