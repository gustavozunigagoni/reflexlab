import reflex as rx
from reflexlab.pages.page12.page12_model import Players
from reflexlab.pages.page12.page12_state import DatabaseTableState
from reflexlab.pages.page12.page12_addeditrow import addeditrow

#Despliega la celda de empleados
def show_player(user: Players):
    """Show a Players in a table row."""
    return rx.table.row(
        rx.table.cell(
            addeditrow(user,"edit"),
        ),
        rx.table.cell(
            _delrow(user),
        ),
        rx.table.cell(user.Name),
        rx.table.cell(user.Team),
        rx.table.cell(user.Number),
        rx.table.cell(user.Position),
        rx.table.cell(user.Age),
        rx.table.cell(user.Height),
        rx.table.cell(user.Weight),
        rx.table.cell(user.College),
        rx.table.cell(user.Salary),
        rx.table.cell(user.id),
    )

def _delrow(user: Players) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("trash-2"),    
                color_scheme="red"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Confirmar borrado"),
            rx.alert_dialog.description(
                "¿Estás seguro de que quieres borrar este registro? Esta acción no se puede deshacer.",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button(
                        "No",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Sí, borrar",
                        color_scheme="red",
                        variant="solid",
                        on_click=DatabaseTableState.delete_player(user.id),
                    ),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
        ),
    )