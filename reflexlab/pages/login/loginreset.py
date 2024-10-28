import reflex as rx
from reflexlab.pages.login.login_state import LoginState


@rx.page(route="/loginreset", title="loginreset")
def loginreset() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.card(
                rx.center(
                    rx.image(
                        src="/logo.jpg",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reinicio de password",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.spacer(height="1em"),
                rx.vstack(
                    rx.text(
                        "Email",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Email de usuario para reiniciar password",
                        type="text",
                        size="3",
                        width="100%",
                        on_change=LoginState.set_emailresetpassword,
                        value=LoginState.emailresetpassword,
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.spacer(height="1em"),
                rx.button(
                    "Reinicio de Password",
                    ize="3",
                    width="100%",
                    on_click=LoginState.loginreset,
                ),
                rx.spacer(height="1em"),
                rx.button(
                    "Cancelar",
                    ize="3",
                    width="100%",
                    on_click=LoginState.loginresetcancel,
                ),
                size="4",
                max_width="28em",
                width="100%",
            ),
            padding="100px",
            justify="center",
            width="100%",
        ),
    )