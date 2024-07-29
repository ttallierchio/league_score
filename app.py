from typing import Union,Annotated
from fastapi import FastAPI
from league_score.services.db_wrapper import DataAccess
app = FastAPI()
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware  
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from league_score.services.user_wrapper import UserService

SECRET = "my_secret"
manager = LoginManager(SECRET, "/login")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080","http://localhost","https://localhost:8080","https://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@manager.user_loader()
def query_user(user_id: str):
    return "user"

@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = form_data.username
    password = form_data.password
    us = UserService()
    user_data = us.validate_user(user,password)
    
    if not user_data:
        # you can return any response or error of your choice
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data={"username": user})
    return {"access_token": access_token}


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