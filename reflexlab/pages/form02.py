import reflex as rx


@rx.page(route="/form02", title="form02")
def form02():
    return rx.form.root(
    rx.form.field(
        rx.flex(
            rx.form.label("Email"),
            rx.form.control(
                rx.input(
                    placeholder="Email Address",
                    type="email",
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
        name="email",
    ),
    rx.form.submit(
        rx.button("Submit"),
        as_child=True,
    ),
    on_submit=lambda form_data: rx.window_alert(
        form_data.to_string()
    ),
    reset_on_submit=True,
)