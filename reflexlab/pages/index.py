import reflex as rx

@rx.page(route="/", title="index")
def index():
    return rx.text("Index")