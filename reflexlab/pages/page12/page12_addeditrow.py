import reflex as rx
from reflexlab.pages.page12.page12_model import Players
from reflexlab.pages.page12.page12_state import DatabaseTableState


def addeditrow(user: Players = Players(), action: str = "edit") -> rx.Component:
    if action == "edit":
        txtbtndialog= "pencil"
        txttitledialog= "Editar Player"
        submit_handler = DatabaseTableState.update_player
    else:
        txtbtndialog= "circle-plus"
        txttitledialog= "Adicionar Player"
        submit_handler = DatabaseTableState.add_player
        
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
                            on_submit=submit_handler,
                        ),
                    ),
                    rx.dialog.close(rx.button("Close")),
                ),
            )
