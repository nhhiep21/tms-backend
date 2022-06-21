"""
    Config module
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Task Management System (TMS) Rest API'

    db_host: str
    db_user: str
    db_port: int
    db_pass: str
    db_name: str
