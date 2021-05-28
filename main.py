
from fastapi import FastAPI
from database import db
from crud.crud_dog import *
from crud.crud_user import *
from schemas import ModelDogs, ModelUser
from auth import *
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from models import *


app = FastAPI()

@app.on_event('startup')
def startup():
    if db.is_closed():
        db.connect()
        db.create_tables([Dog, User])
    
@app.on_event('shutdown')
def shutdown():
    if not db.is_closed():
        db.close()


@app.post("/api/users")
async def create_users(user:ModelUser):
    return create_user(user.id, user.name, user.last_name, user.email)


@app.get("/api/users/{id}")
async def get_user_id(id:str):
    user=get_user(id)
    if not user:
        return "Usuario no encontrado"
    else:
        return user


@app.delete("/api/users/{id}")
async def delete_users(id:str):
    return delete_user(id)


@app.put("/api/users")
async def update_user(user:ModelUser):
    return update_user_(user)


@app.post("/api/dogs")
async def create_dogs(id:str, name:str, is_adopted:bool, id_user:str, form_data:OAuth2PasswordRequestForm = Depends()):
    user = getUser(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail ="Usuario o contraseña incorrecto",
            headers = {"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(
        data={"password" : user["password"],
        "sub" : user["username"]}
    )
    if get_current_user(token):
        return create_dog(id_user, id,name, get_dog_image_api(), is_adopted)


@app.get("/api/dogs")
async def dogs():
    result = get_list_dogs()
    return list(result)


@app.get("/api/dogs/{name}")
async def get_dog_for_name(name:str):
    dog = get_dog(name)
    if not dog:
        return "No existe registro"
    return list(dog)

@app.get("/api/dogs/is_adopted/{}")
async def dog_is_adopted(adopted:bool = True):
    adopted = get_dog_is_adopted(adopted)
    return list(adopted)
   

@app.delete("/api/dogs/{name}")
async def eliminar_dog(name:str):
    return delete_dog(name)
    

@app.put("/api/dogs")
async def update_dog(dog:ModelDogs):
    return update_dog(dog)


