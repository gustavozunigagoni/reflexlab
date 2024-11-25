import reflex as rx

class User(rx.Base):
    name: str
    email: str
    gender: str


class State(rx.State):
    opened: bool = False
    users: list[User] = [
        User(
            name="Danilo Sousa",
            email="danilo@example.com",
            gender="Male",
        ),
        User(
            name="Zahra Ambessa", 
            email="zahra@example.com",
            gender="Female",
        ),
    ]

    @rx.event
    def dialog_open(self):
        self.opened = ~self.opened

def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
        rx.table.cell(
            rx.button(
                "Open Dialog",
                on_click=State.dialog_open
            )
        )
    )

@rx.page(route="/page14", title="page14")
def page14():
    return rx.vstack(
        rx.dialog.root(
            rx.dialog.content(
                rx.dialog.title("Welcome to Reflex!"),
                rx.dialog.description(
                    "This is a dialog component. You can render anything you want in here.",
                ),
                rx.button(
                        "Close Dialog",
                        on_click=State.dialog_open
                ),
            ),
            open=State.opened,
        ),
         rx.button(
                "Open Dialog",
                on_click=State.dialog_open
            ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                    rx.table.column_header_cell("Actions"),
                ),
            ),
            rx.table.body(
                rx.foreach(State.users, show_user),
            ),
        )
    )