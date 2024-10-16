import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/GanttChart-updated.csv"
)

column_defs = [
    ag_grid.column_def(field="Task", filter=True),
    ag_grid.column_def(
        field="Start", filter=ag_grid.filters.date
    ),
    ag_grid.column_def(
        field="Duration", filter=ag_grid.filters.number
    ),
    ag_grid.column_def(
        field="Resource", filter=ag_grid.filters.text
    ),
]



@rx.page(route="/page05", title="page05")
def page05():
    return rx.vstack(
            rx.heading("ag grid se pueden pueden activar filtros en las columnas y parametrizar los mismos"),
            ag_grid(
                id="ag_grid_basic_headers",
                row_data=df.to_dict("records"),
                column_defs=column_defs,
                width="80%",
                height="40vh",
            ),
            align="center"
    )