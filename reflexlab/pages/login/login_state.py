import reflex as rx
import json
import requests

class LoginState(rx.State):
    id_token_json: str = rx.LocalStorage()
    username: str = ""
    password: str = ""

    def login(self):
        print("VOOOOOOYYYYYY")
        try:
            response = requests.post(
                'http://192.168.100.45:8080/realms/reflexlab/protocol/openid-connect/token',
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                data={
                    'client_id': 'reflexlab',
                    'client_secret': 'o2avmglPR7IrEp2ddpj25PAHxN8kmQvf',
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
                return rx.redirect("/page12")  
            return None
        except Exception as exc:
            print(f"Error en la autenticación: {exc}")
            return None

    @rx.var
    def token_is_valid(self) -> bool:
        try:
            token_data = json.loads(self.id_token_json)
            if not token_data:
                return False

            response = requests.get(
                'http://192.168.100.45:8080/realms/reflexlab/protocol/openid-connect/userinfo',
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