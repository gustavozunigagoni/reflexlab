import reflex as rx

class DataTableState(rx.State):
    cols: list[dict] = [
        {"title": "Name", "type": "str"},
        {"title": "Email", "type": "str"},
        {"title": "Age", "type": "int"},
    ]
    data: list[list[str]] = [
        ["John Doe", "john@example.com", "30"],
        ["Jane Smith", "jane@example.com", "25"],
        ["Bob Johnson", "bob@example.com", "35"],
    ]

    def update_cell(self, row: int, col: int, value: str):
        self.data[row][col] = value

def show_user(user: list, index: int):
    return rx.table.row(
        rx.foreach(
            DataTableState.cols,
            lambda col, col_index: rx.table.cell(
                rx.input(
                    value=user[col_index],
                    on_change=lambda value: DataTableState.update_cell(index, col_index, value),
                )
            )
        )
    )

@rx.page(route="/page11", title="page11")
def page11():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.foreach(
                    DataTableState.cols,
                    lambda col: rx.table.column_header_cell(col["title"])
                )
            )
        ),
        rx.table.body(
            rx.foreach(
                DataTableState.data,
                show_user
            )
        ),
        width="100%",
    )