import reflex as rx
import csv
import io
import json
from sqlmodel import select,Field, Session, create_engine, asc, or_, func, SQLModel
from reflexlab.pages.page12.page12_model import Players
from reflexlab.pages.page12.page12_state import DatabaseTableState
from reflexlab.pages.page12.page12_showrows import show_player
from reflexlab.pages.page12.page12_addeditrow import addeditrow
from reflexlab.pages.login.login_state import LoginState


@rx.page(route="/page12", title="page12",on_load=LoginState.check_login )
def page12():
    return rx.vstack(
         rx.hstack(
            rx.button(
                "Logout",
                on_click=LoginState.logout,
            ),
            spacing="7",
        ),
        rx.hstack(
            rx.select(
                ["10", "20", "30", "50"],
                placeholder="Elementos por página",
                on_change=DatabaseTableState.update_limit,
                default_value="10"
            ),
            rx.button(
                "Prev",
                on_click=DatabaseTableState.prev_page,
            ),
            rx.text(
                f"Page {DatabaseTableState.page_number} / {DatabaseTableState.total_pages}"
            ),
            rx.button(
                "Next",
                on_click=DatabaseTableState.next_page,
            ),
        ),
        rx.hstack(
            rx.button(
                "Download as CSV",
                on_click=DatabaseTableState.download_csv_data,
            ),
            spacing="7",
        ),
        rx.select(
            ["id","Name","Team", "Position"],
            placeholder="Ordenado por: Team",
            on_change=lambda value: DatabaseTableState.sort_values(
                value
            ),default_value="id"
        ),
        rx.input(
            placeholder="Search here...",
            on_change=lambda value: DatabaseTableState.filter_values(
                value
            ),
        ),
        addeditrow(action='add'),
        rx.scroll_area(
            rx.flex(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Accions", col_span=3),
                            rx.table.column_header_cell("Name"),
                            rx.table.column_header_cell("Team"),
                            rx.table.column_header_cell("Number"),
                            rx.table.column_header_cell("Position"),
                            rx.table.column_header_cell("Age"),
                            rx.table.column_header_cell("Height"),
                            rx.table.column_header_cell("Weight"),
                            rx.table.column_header_cell("College"),
                            rx.table.column_header_cell("Salary"),
                            rx.table.column_header_cell("id"),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(
                            DatabaseTableState.users, show_player
                        )
                    ),
                    on_mount=DatabaseTableState.load_entries,
                    width="100%",
                ),
                style={"width": 800},
            ),
            type="always",
            scrollbars="both",
            style={"height": 700},
        )
    )