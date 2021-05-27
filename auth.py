from datetime import timedelta, datetime
from typing import Optional
from config import *
from jose import JWTError, jwt
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")
fake_users_db = {
    "dperezc21" : {
        "username" : "dperezc21",
        "full_name" : "davier perez",
        "email" : "davierperez11.2@gmail.com",
        "password" : "davier",
        "disabled" : False,
    }
}


def getUser(db, username:str, password:str):
    if username in db and db[username]["password"] == password:
        user_dict = db[username]
        return user_dict


def authenticate_user(fake_db, username:str):
    if not username in fake_db:
        return False
    user_dict = fake_db[username]
    return user_dict
    

def create_access_token(data:dict, expires_delta:Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now()+expires_delta
    else:
        expire = datetime.now() + timedelta(days = 30)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt


def get_current_user(token):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate" : "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = username
    except JWTError:
        raise credentials_exception
    user = authenticate_user(fake_users_db, username = token_data)
    if user is None:
        raise credentials_exception
    return user





