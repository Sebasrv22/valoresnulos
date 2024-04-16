import pandas as pd

# Cargando el archivo notas_credito.xlsx
df = pd.read_excel('notas_credito.xlsx')
print(df.head())

def fill_missing_values(df):
    # Sustituyendo valores nulos en 'CVE_VEND' con "Sin Asignar"
    df['CVE_VEND'].fillna("Sin Asignar", inplace=True)
    
    # Sustituyendo valores nulos en 'CVE_PEDI' con "No disponible"
    df['CVE_PEDI'].fillna("No disponible", inplace=True)
    
    # Sustituyendo valores nulos en 'FECHA_CANCELA' con "No cancelado"
    df['FECHA_CANCELA'].fillna("No cancelado", inplace=True)
    
    return df

# Llamando a la función para tratar valores nulos
df = fill_missing_values(df)

# Guardando el DataFrame limpio como un archivo CSV
df.to_csv('notas_credito_clean.csv', index=False)

# Mostrando información del DataFrame para confirmar que no hay valores nulos
print("\nInformación después de limpiar:")
print(df.info())
print(df.head())
