from typing import Union

from fastapi import FastAPI
from league_score.services.db_wrapper import DataAccess
app = FastAPI()
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from league_score.services.user_wrapper import UserService
SECRET = "my_secret"
manager = LoginManager(SECRET, "/login")

@manager.user_loader()
def query_user(user_id: str):
    return "user"

@app.get("/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    user = "test"
    password = "password"
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != password:
        raise InvalidCredentialsException

    return {"status": "Success"}


@app.get("/generate_admin")
def gen_admin():
    try:
        us = UserService()
        us.generate_admin_user()
    except Exception as e:
        print(e)
        print("user already created")
        return 400
    
@app.get("/")
def read_root():
    da = DataAccess()
    with da.connect() as conn:
        print(conn)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}