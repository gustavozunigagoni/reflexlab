import reflex as rx
from reflexlab.pages.page12.page12_model import Players
from reflexlab.pages.page12.page12_state import DatabaseTableState


#Despliega la celda de empleados
def show_player(user: Players):
    """Show a Players in a table row."""
    return rx.table.row(
        rx.table.cell(
            _editrow(user,"edit"),
        ),
        rx.table.cell(
            _editrow(user,"add"),
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

def _editrow(user: Players, action: str = "edit") -> rx.Component:
    if action == "edit":
        txtbtndialog= "pencil"
        txttitledialog= "Ediat Player"
    else:
        txtbtndialog= "circle-plus"
        txttitledialog= "Adicionar Player"

    return rx.dialog.root(
                rx.dialog.trigger(rx.button(
                    rx.icon(txtbtndialog)
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title(txttitledialog),
                    rx.dialog.description(
                        rx.form(
                            rx.vstack(
                                rx.el.input(
                                    type="hidden",
                                    name="id",
                                    value=user.id,
                                    readonly=True
                                ),
                                rx.form.field(
                                    rx.flex(
                                        rx.form.label("name"),
                                        rx.form.control(
                                            rx.input(
                                                placeholder="name",
                                                default_value=user.Name,
                                                required=True
                                            ),
                                            as_child=True,
                                        ),
                                        rx.form.message(
                                            DatabaseTableState.error_message,
                                            match="valueMissing",
                                            force_match=DatabaseTableState.has_error,
                                            color="var(--red-11)",
                                        ),
                                        direction="column",
                                        spacing="2",
                                        align="stretch",
                                    ),                          
                                    name="name"
                                ),
                                #rx.form.field(name="team", default_value=user.Team),
                                #rx.form.field(name="number", default_value=user.Number),
                                #rx.form.field(name="position", default_value=user.Position),
                                #rx.form.field(name="age", default_value=user.Age),
                                #rx.form.field(name="height", default_value=user.Height),
                                #rx.form.field(name="weight", default_value=user.Weight),
                                #rx.form.field(name="college", default_value=user.College),
                                #rx.form.field(name="salary", default_value=user.Salary),
                                rx.button("Submit", type="submit"),
                            ),
                            on_submit=DatabaseTableState.update_player,
                        ),
                    ),
                    rx.dialog.close(rx.button("Close")),
                ),
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