import pandas as pd
import pyodbc
import numpy as np

# Conexión a SQL Server
DATABASE_URL= "mssql+pyodbc://rxuseradquirencias:rxUserAdquirenciaTarjetasPasswrd#01@crsjce010440vm.daviviendacr.com/AdquirenciaTarjetas?driver=ODBC+Driver+17+for+SQL+Server"

conn_str = (
    "DRIVER={SQL Server};"
    "SERVER=crsjce010440vm.daviviendacr.com;"  # Cambia 'your_server_name' por el nombre de tu servidor
    "DATABASE=AdquirenciaTarjetas;"  # Cambia 'your_database_name' por el nombre de tu base de datos
    "UID=rxuseradquirencias;"  # Cambia 'your_username' por tu usuario
    "PWD=rxUserAdquirenciaTarjetasPasswrd#01;"  # Cambia 'your_password' por tu contraseña
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Leer el archivo CSV
csv_file_path = 'https://media.geeksforgeeks.org/wp-content/uploads/nba.csv'  # Cambia a la ruta de tu archivo CSV
df = pd.read_csv(csv_file_path)

# Definir el nombre de la tabla donde se insertarán los datos
table_name = 'Players'  # Cambia a tu nombre de tabla

# Insertar los datos en la tabla
for index, row in df.iterrows():
    print(row['Name'])
    if pd.notna(row['Name']) and pd.notna(row['Team']) and pd.notna(row['Number']) and pd.notna(row['Position']) and \
       pd.notna(row['Age']) and pd.notna(row['Height']) and pd.notna(row['Weight']) and pd.notna(row['College']) and \
       pd.notna(row['Salary']):
        cursor.execute(f"""
            INSERT INTO {table_name} (Name,Team,Number,Position,Age,Height,Weight,College,Salary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            row['Name'], row['Team'], row['Number'], row['Position'], row['Age'], row['Height'], row['Weight'], 
            row['College'], row['Salary'] if pd.notna(row['Salary']) else None  # Manejar valores NULL
    )

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Datos insertados correctamente.")
