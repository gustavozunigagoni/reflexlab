import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridThemeState(rx.State):
    """The app state."""

    theme: str = "quartz"
    themes: list[str] = [
        "quartz",
        "balham",
        "alpine",
        "material",
    ]

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(
        field="pop", header_name="Population"
    ),
    ag_grid.column_def(
        field="lifeExp", header_name="Life Expectancy"
    ),
]


@rx.page(route="/page10", title="page10")
def page10():
    return rx.vstack(
            rx.heading("ag grid el Temas"),
            rx.hstack(
                rx.text("Theme:"),
                rx.select(
                    AGGridThemeState.themes,
                    value=AGGridThemeState.theme,
                    on_change=AGGridThemeState.set_theme,
                ),
            ),
            ag_grid(
                id="ag_grid_basic_themes",
                row_data=df.to_dict("records"),
                column_defs=column_defs,
                theme=AGGridThemeState.theme,
                width="80%",
                height="40vh",
            ),
            align="center"
    )