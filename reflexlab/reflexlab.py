"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflexlab.backend.loadenv import settings
from reflexlab.pages.index import index
from reflexlab.pages.page01 import page01
from reflexlab.pages.page02 import page02
from reflexlab.pages.page03 import page03
from reflexlab.pages.page04 import page04
from reflexlab.pages.page05 import page05
from reflexlab.pages.page06 import page06
from reflexlab.pages.page07 import page07
from reflexlab.pages.page08 import page08
from reflexlab.pages.page09 import page09

from rxconfig import config

print(settings.db_host)

class State(rx.State):
    """The app state."""

    ...


app = rx.App()
app.add_page(index)
app.add_page(page01)
app.add_page(page02)
app.add_page(page03)
app.add_page(page04)
app.add_page(page05)
app.add_page(page06)
app.add_page(page07)
app.add_page(page08)
app.add_page(page09)
