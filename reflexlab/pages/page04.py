import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

column_defs = [
    ag_grid.column_def(
        field="country", header_name="Country", filter=True
    ),
    ag_grid.column_def(
        field="pop", header_name="Population"
    ),
    ag_grid.column_def(
        field="lifeExp",
        header_name="Life Expectancy",
        filter=True,
    ),
]


@rx.page(route="/page04", title="page04")
def page04():
    return rx.vstack(
            rx.heading("ag grid se pueden pueden activar filtros en las columnas"),
            ag_grid(
                id="ag_grid_basic_headers",
                row_data=df.to_dict("records"),
                column_defs=column_defs,
                width="80%",
                height="40vh",
            ),
            align="center"
    )