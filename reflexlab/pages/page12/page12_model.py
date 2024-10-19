import reflex as rx


# Modelo de players
class Players(rx.Model, table=True):
    Name: str
    Team: str
    Number: float
    Position: str
    Age: float
    Height: str
    Weight: float
    College: str
    Salary: float