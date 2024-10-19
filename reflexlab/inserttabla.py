import pandas as pd
import psycopg2
import numpy as np

##Esta es la estructura de la table de pruebas
#CREATE TABLE IF NOT EXISTS public.players
#(
#    "Name" character varying(100) COLLATE pg_catalog."default",
#    "Team" character varying(100) COLLATE pg_catalog."default",
#    "Number" double precision,
#    "Position" character varying(10) COLLATE pg_catalog."default",
#    "Age" double precision,
#    "Height" character varying(10) COLLATE pg_catalog."default",
#    "Weight" double precision,
#    "College" character varying(100) COLLATE pg_catalog."default",
#    "Salary" double precision,
#    id character varying(50) NOT NULL DEFAULT gen_random_uuid()::varchar, -- Convertimos UUID a varchar
#   CONSTRAINT pk_player PRIMARY KEY (id)
#);
##

# Configurar la cadena de conexión para PostgreSQL
conn_str = (
    "dbname='bancogzg' "
    "user='postgres' "
    "password='GzgAdoZu2' "
    "host='192.168.100.45' "
    "port='5432'"
)

# Conexión a PostgreSQL
conn = psycopg2.connect(conn_str)
cursor = conn.cursor()

# Leer el archivo CSV
csv_file_path = 'https://media.geeksforgeeks.org/wp-content/uploads/nba.csv'
df = pd.read_csv(csv_file_path)

# Definir el nombre de la tabla donde se insertarán los datos
table_name = 'Players'

# Insertar los datos en la tabla
for index, row in df.iterrows():
    print(row['Name'])
    if pd.notna(row['Name']) and pd.notna(row['Team']) and pd.notna(row['Number']) and pd.notna(row['Position']) and \
       pd.notna(row['Age']) and pd.notna(row['Height']) and pd.notna(row['Weight']) and pd.notna(row['College']) and \
       pd.notna(row['Salary']):
        cursor.execute(f"""
            INSERT INTO {table_name} ("Name", "Team", "Number", "Position", "Age", "Height", "Weight", "College", "Salary")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (row['Name'], row['Team'], row['Number'], row['Position'], row['Age'], row['Height'], row['Weight'], 
            row['College'], row['Salary'] if pd.notna(row['Salary']) else None)
        )

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Datos insertados correctamente.")
