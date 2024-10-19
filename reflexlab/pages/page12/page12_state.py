import reflex as rx
from sqlmodel import select, Session, asc, or_, func
import json
import csv
import io
from reflexlab.pages.page12.page12_model import Players
from reflexlab.pages.page12.page12_engine import engine

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