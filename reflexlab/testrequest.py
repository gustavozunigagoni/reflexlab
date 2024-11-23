import requests

url = 'http://192.168.100.45:8080/realms/reflexlab/protocol/openid-connect/token'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'client_id': 'reflexlab',
    'client_secret': 'o2avmglPR7IrEp2ddpj25PAHxN8kmQvf',
    'username': 'gustavo',
    'password': 'GzgAdoZu2',
    'grant_type': 'password',
    'scope': 'openid'
}

try:
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # Lanza un error si el código de estado no es 2xx
    print("Respuesta del servidor:", response.json())
except requests.exceptions.RequestException as e:
    print("Error en la solicitud:", e)
