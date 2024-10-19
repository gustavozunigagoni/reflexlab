import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv"
)


#se puede sacar los titulos de las columnas de el df directamente

@rx.page(route="/page02", title="page02")
def page02():
    return rx.vstack(
            rx.heading("ag grid sacando los titulos directamente de los datos"),
            ag_grid(
                id="ag_grid_basic_2",
                row_data=df.to_dict("records"),
                column_defs=[{"field": i} for i in df.columns],
                width="80%",
                height="80vh",
            ),
            align="center"
    )