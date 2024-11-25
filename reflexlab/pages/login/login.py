import reflex as rx
from reflexlab.pages.login.login_state import LoginState

@rx.page(route="/login", title="login")
def login() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.center(
                            rx.image(
                                src="/logo.jpg",
                                width="2.5em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Inicio de session",
                                size="6",
                                as_="h2",
                                text_align="center",
                                width="100%",
                            ),
                            direction="column",
                            spacing="5",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Usuario",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                name="username",
                                placeholder="Su login de usuario",
                                type="text",
                                size="3",
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.text(
                                    "Clave",
                                    size="3",
                                    weight="medium",
                                ),
                                rx.link(
                                    "Olvido su clave?",
                                    href="/loginreset",
                                    size="3",
                                ),
                                justify="between",
                                width="100%",
                            ),
                            rx.input(
                                name="password",
                                placeholder="Clave",
                                type="password",
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.form.submit(
                            rx.button(
                                "Inicio session",
                                size="3",
                                width="100%",
                            ),
                            as_child=True,
                        ),
                        rx.cond(
                            LoginState.errlogin != "",
                            rx.hstack(
                                rx.text(
                                    LoginState.errlogin,
                                    size="3",
                                    weight="medium",
                                    color="red"
                                ),
                                justify="between",
                                width="100%",
                            ),
                        ),
                        rx.center(
                            rx.text("Nuevo aqui?", size="3"),
                            rx.link("Registro", href="/loginregistry", size="3"),
                            opacity="0.8",
                            spacing="2",
                            direction="row",
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    size="4",
                    max_width="28em",
                    width="100%",
                ),
                padding="100px",
                justify="center",
                width="100%",
            ),
        ),
        on_submit=LoginState.login
    )
