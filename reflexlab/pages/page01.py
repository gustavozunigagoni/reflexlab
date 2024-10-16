import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv"
)

column_defs = [
    ag_grid.column_def(field="direction"),
    ag_grid.column_def(field="strength"),
    ag_grid.column_def(field="frequency"),
]

@rx.page(route="/page01", title="page01")
def page01():
    return rx.vstack(
            rx.heading("ag grid simple"),
            ag_grid(
                id="ag_grid_basic_1",
                row_data=df.to_dict("records"),
                column_defs=column_defs,
                width="80%",
            ),
            align="center"
    )