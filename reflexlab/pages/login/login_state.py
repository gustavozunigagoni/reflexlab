import reflex as rx
import json
import requests
from reflexlab.backend.loadenv import settings

class LoginState(rx.State):
    id_token_json: str = rx.LocalStorage()
    username: str = ""
    password: str = ""
    errlogin: str = ""
    emailresetpassword: str = ""

    def login(self):
        try:
            response = requests.post(
                f'{settings.keycloak_server}/realms/{settings.keycloak_realm}/protocol/openid-connect/token',
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                data={
                    'client_id': settings.keycloak_client_id,
                    'client_secret': settings.keycloak_client_secret,
                    'username': self.username,
                    'password': self.password,
                    'grant_type': 'password',
                    'scope': 'openid'
                }
            )
            print(response.status_code)
            if response.status_code == 200:
                self.id_token_json = json.dumps(response.json())
                print(self.id_token_json)
                self.errlogin = ""
                return rx.redirect("/page12")  
            else:
                self.errlogin = "ERROR: usuario o clave invalido"
                return None
        except Exception as exc:
            self.errlogin = f"Error en la autenticación: {exc}"

            return None

    @rx.var
    def token_is_valid(self) -> bool:
        try:
            token_data = json.loads(self.id_token_json)
            if not token_data:
                return False

            response = requests.get(
                f'{settings.keycloak_server}/realms/{settings.keycloak_realm}/protocol/openid-connect/userinfo',
                headers={'Authorization': f'Bearer {token_data["access_token"]}'}
            )
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception:
            return False

    def check_login(self):
        if not self.token_is_valid:
            return rx.redirect("/login")

    def logout(self):
        self.id_token_json = ""
        return rx.redirect("/login")
    
    def loginresetcancel(self):
        return rx.redirect("/login")
    
    def loginreset(self):
        try:
            print("VOOOOOYYYYY")
            response = requests.post(
                f'{settings.keycloak_server}/realms/{settings.keycloak_realm}/protocol/openid-connect/token',
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                data={
                    'client_id': settings.keycloak_client_id,
                    'client_secret': settings.keycloak_client_secret,
                    'username': settings.admin_login_username,
                    'password': settings.admin_login_password,
                    'grant_type': 'password',
                    'scope': 'openid'
                }
            )
            if response.status_code == 200:
                token_data = json.dumps(response.json())
                token_data = json.loads(token_data)
                aux_token = token_data["access_token"]
                response = requests.get(
                    f'{settings.keycloak_server}/admin/realms/{settings.keycloak_realm}/users?email={self.emailresetpassword}',
                    headers={'Authorization': f'Bearer {aux_token}'}
                )
                if response.status_code == 200:
                    token_data = json.dumps(response.json())
                    token_data = json.loads(token_data)
                    aux_id = [item['id'] for item in token_data][0]
                    response = requests.put(
                        f'{settings.keycloak_server}/admin/realms/{settings.keycloak_realm}/users/{aux_id}/execute-actions-email',
                        headers={'Authorization': f'Bearer {aux_token}','Content-Type': 'application/json'},
                        data='["UPDATE_PASSWORD"]'
                    )
                    if response.status_code == 204:
                        pass
                    else:
                        pass
            else:
                return None

        except Exception as exc:
            self.errlogin = f"Error en la autenticación: {exc}"
            print(self.errlogin)
            return None
        