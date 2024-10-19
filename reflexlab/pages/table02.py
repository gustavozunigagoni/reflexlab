import reflex as rx
import csv
import io
import json
from sqlmodel import select,Field, Session, create_engine, asc, or_, func, SQLModel


#  Configuracion de base de datos
#DATABASE_URL= "mssql+pyodbc://rxuseradquirencias:rxUserAdquirenciaTarjetasPasswrd#01@crsjce010440vm.daviviendacr.com/AdquirenciaTarjetas?driver=ODBC+Driver+17+for+SQL+Server"
DATABASE_URL= "postgresql://postgres:GzgAdoZu2@192.168.100.45:5432/bancogzg"
engine = create_engine(DATABASE_URL,echo=True)

# Funcion para obtener una session de base de datos
def get_session():
    with Session(engine) as session:
        yield session

# Modelo de players
class Players(rx.Model, table=True):
    Name: str
    Team: str
    Number: float
    Position: str
    Age: float
    Height: str
    Weight: float
    College: str
    Salary: float

#State de la tabla de la base de datos
class DatabaseTableState(rx.State):
    users: list[Players] = []

    sort_value = ""
    search_value = ""

    total_items: int
    offset: int = 0
    limit: int = 10

    def update_limit(self, new_limit: str):
        self.limit = int(new_limit)
        self.offset = 0  # Reinicia la página a la primera cuando cambia el límite
        self.load_entries()

    @rx.var(cache=True)
    def page_number(self) -> int:
        return (
            (self.offset // self.limit)
            + 1
            + (1 if self.offset % self.limit else 0)
        )

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return self.total_items // self.limit + (
            1 if self.total_items % self.limit else 0
        )
    
    def prev_page(self):
        self.offset = max(self.offset - self.limit, 0)
        self.load_entries()

    def next_page(self):
        if self.offset + self.limit < self.total_items:
            self.offset += self.limit
        self.load_entries()

    def _get_total_items(self, session):
        """Return the total number of items in the Customer table."""
        self.total_items = session.exec(
            select(func.count(Players.id))
        ).one()

    def load_entries(self) -> list[Players]:
        """Get all users from the database."""
        with Session(engine) as session:
            query = select(Players)

            if self.search_value != "":
                search_value = f"%{self.search_value.lower()}%"
                query = query.where(
                    or_(
                        Players.Name.ilike(search_value),
                        Players.Team.ilike(search_value),
                        Players.Position.ilike(search_value),
                    )
                )

            # Siempre incluir una cláusula ORDER BY
            if self.sort_value != "":
                sort_column = getattr(Players, self.sort_value)
            else:
                # Ordenar por Team por defecto si no se especifica un valor de ordenación
                sort_column = Players.id
            order = asc(sort_column)
            query = query.order_by(order)

            # Aplicar paginación
            query = query.offset(self.offset).limit(self.limit)

            self.users = session.exec(query).all()
            self._get_total_items(session)
    
    def update_player(self, form_data: dict):
        with Session(engine) as session:
            player = session.get(Players, form_data["id"])
            if player:
                for key, value in form_data.items():
                    if key != "id":
                        setattr(player, key.capitalize(), value)
                session.commit()
        self.load_entries()
    
    def sort_values(self, sort_value):
        self.sort_value = sort_value
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def fetch_all_records(self, limit: int = 5000) -> list[Players]:
        with Session(engine) as session:
            query = select(Players).limit(limit)
            return session.exec(query).all()
  
    def get_json_data(self):
        records = self.fetch_all_records()
        return json.dumps([record.dict() for record in records])

    def _convert_to_csv(self) -> str:
        all_records = self.fetch_all_records()

        fieldnames = list(Players.__fields__)

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for record in all_records:
            writer.writerow(record.dict())

        csv_data = output.getvalue()
        output.close()
        return csv_data

    def download_csv_data(self):
        csv_data = self._convert_to_csv()
        return rx.download(
            data=csv_data,
            filename="data.csv",
        )


#Despliega la celda de empleados
def show_player(user: Players):
    """Show a Players in a table row."""
    return rx.table.row(
        rx.table.cell(
            rx.dialog.root(
                rx.dialog.trigger(rx.button("Edit")),
                rx.dialog.content(
                    rx.dialog.title("Edit Player"),
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
                                            "Please enter a valid email",
                                            match="typeMismatch",
                                        ),
                                        direction="column",
                                        spacing="2",
                                        align="stretch",
                                    ),                          
                                    name="name"
                                ),
                                rx.form.field(name="team", default_value=user.Team),
                                rx.form.field(name="number", default_value=user.Number),
                                rx.form.field(name="position", default_value=user.Position),
                                rx.form.field(name="age", default_value=user.Age),
                                rx.form.field(name="height", default_value=user.Height),
                                rx.form.field(name="weight", default_value=user.Weight),
                                rx.form.field(name="college", default_value=user.College),
                                rx.form.field(name="salary", default_value=user.Salary),
                                rx.button("Submit", type="submit"),
                            ),
                            on_submit=DatabaseTableState.update_player,
                        ),
                    ),
                    rx.dialog.close(rx.button("Close")),
                ),
            )
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

@rx.page(route="/table02", title="table02")
def table02():
    return rx.vstack(
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
            #rx.button(
            #    "Download as JSON",
            #    on_click=rx.download(
            #        data=DatabaseTableState.get_json_data(),
            #        filename="data.json",
            #    ),
            #),
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
        rx.table.root(
            rx.table.header(
                rx.table.row(
                     rx.table.column_header_cell("Editar"),
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
    )