import pandas as pd

# Cargando el archivo precios_productos.xlsx
df = pd.read_excel('precios_productos.xlsx')
print(df.head())

def fill_missing_values(df):
    # Sustituyendo valores nulos en 'NOMBRE_VENDEDOR' con "Sin Asignar"
    df['NOMBRE_VENDEDOR'].fillna("Sin Asignar", inplace=True)
    
    return df

# Llamando a la función para tratar valores nulos
df = fill_missing_values(df)

# Guardando el DataFrame limpio como un archivo CSV
df.to_csv('precios_productos_clean.csv', index=False)

# Mostrando información del DataFrame para confirmar que no hay valores nulos
print("\nInformación después de limpiar:")
print(df.info())
print(df.head())
