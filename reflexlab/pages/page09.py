import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridEditingState(rx.State):
    data_df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
    )

    @rx.var
    def data(self) -> list[dict]:
        return self.data_df.to_dict("records")

    def cell_value_changed(self, row, col_field, new_value):
        self.data_df.at[row, col_field] = new_value
        yield rx.toast(
            f"Cell value changed, Row: {row}, Column: {col_field}, New Value: {new_value}"
        )

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(
        field="pop",
        header_name="Population",
        editable=True,
        cell_editor=ag_grid.editors.number,
    ),
    ag_grid.column_def(
        field="continent",
        editable=True,
        cell_editor=ag_grid.editors.select,
        cell_editor_params={
            "values": [
                "Asia",
                "Europe",
                "Africa",
                "Americas",
                "Oceania",
            ]
        },
    ),
]


@rx.page(route="/page09", title="page09")
def page09():
    return rx.vstack(
            rx.heading("ag grid el order es default pero se puede s=deartivar en las columnas"),
            ag_grid(
                id="ag_grid_basic_headers",
                row_data=AGGridEditingState.data,
                column_defs=column_defs,
                on_cell_value_changed=AGGridEditingState.cell_value_changed,
                row_selection="multiple",
                pagination=True,
                pagination_page_size=10,
                pagination_page_size_selector=[10, 40, 100],
                width="80%",
                height="40vh",
            ),
            align="center"
    )