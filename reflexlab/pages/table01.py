import reflex as rx
import pandas as pd

nba_data = pd.read_csv(
    "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"
)


@rx.page(route="/table01", title="table01")
def table01():
    return rx.vstack(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Full name", width="20%"),
                            rx.table.column_header_cell("Email", width="40%"),
                            rx.table.column_header_cell("Group", width="40%"),
                        ),
                    ),
                    rx.table.body(
                        rx.table.row(
                            rx.table.cell(
                                rx.dialog.root(
                                    rx.dialog.trigger(rx.button("Danilo Sousa")),
                                    rx.dialog.content(
                                        rx.dialog.title("Danilo Sousa"),
                                        rx.dialog.description(
                                            "Email: danilo@example.com\nGroup: Developer"
                                        ),
                                        rx.dialog.close(
                                            rx.button("Close", size="3"),
                                        ),
                                        max_width="100vw",  # Ajusta este valor según sea necesario
                                        width="80vw", 
                                        position="fixed",
                                        top="0",
                                        left="50%",
                                        transform="translateX(-50%)",
                                    ),
                                ),
                            ),
                            rx.table.cell("danilo@example.com"),
                            rx.table.cell("Developer"),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.link("Zahra Ambessa", href=f"/employee?email=zahra@example.com")),
                            rx.table.cell("zahra@example.com"),
                            rx.table.cell("Admin"),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.link("Jasper Eriks", href=f"/employee?email=jasper@example.comm")),
                            rx.table.cell("jasper@example.com"),
                            rx.table.cell("Developer"),
                        ),
                    ),
                    width="80%",
                ),            
            align="center"  
        ),