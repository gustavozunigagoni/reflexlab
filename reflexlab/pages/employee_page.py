import reflex as rx

class EmployeeState(rx.State):
    @rx.var
    def employee_email(self):
        return self.router.page.params.get("email", "No email provided")

@rx.page(route="/employee", title="employee")
def employee_page():
    return rx.vstack(
        rx.text("Employee Email:"),
        rx.text(EmployeeState.employee_email),
        rx.link("Regreso", href=f"/table01")
    )

