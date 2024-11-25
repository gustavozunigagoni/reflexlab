import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    admin_login_username: str
    admin_login_password: str
    admin_login_id: str
    keycloak_server: str
    keycloak_realm: str
    keycloak_client_id: str
    keycloak_client_secret: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    db_user: str

settings = Settings()