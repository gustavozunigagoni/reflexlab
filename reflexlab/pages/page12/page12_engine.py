import reflex as rx
from sqlmodel import Session, create_engine

#  Configuracion de base de datos
#DATABASE_URL= "mssql+pyodbc://rxuseradquirencias:rxUserAdquirenciaTarjetasPasswrd#01@crsjce010440vm.daviviendacr.com/AdquirenciaTarjetas?driver=ODBC+Driver+17+for+SQL+Server"
DATABASE_URL= "postgresql://postgres:GzgAdoZu2@192.168.100.45:5432/bancogzg"
engine = create_engine(DATABASE_URL,echo=True)

# Funcion para obtener una session de base de datos
def get_session():
    with Session(engine) as session:
        yield session
