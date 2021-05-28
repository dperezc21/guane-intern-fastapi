from models import Dog, User
import json
from config import API
import requests
from datetime import datetime


def get_dog_image_api():
    response = requests.get(API)
    if response.status_code == 200:
        pinture_ = json.loads(response.text)
        return pinture_["message"]


def get_list_dogs():
    return Dog.select().offset(0).limit(100)


def get_dog(name:str):
    return Dog.select().where(Dog.name == name)


def get_dog_is_adopted(adopted:bool):
    return Dog.select().where(Dog.is_adopted == adopted).offset(0).limit(100)


def create_dog(id_user_:str, id_:str, name_:str, pinture_:str, is_adopted_:bool):
    user = User.select().where(User.id==id_user_).first()
    if user:
        dog = Dog.create(
            id_user = id_user_,
            id = id_,
            name = name_,
            pinture = pinture_,
            is_adopted = is_adopted_,
            create_date = datetime.now()
        )
        if dog:
            return "dog created"
        else:
            return False
    else:
        return "Registro del usuario con Id: {} no existe".format(id_user_)
    

def delete_dog(name:str):
    dog_deleted = Dog.select().where(Dog.name == name).first()
    if dog_deleted:
        dog_deleted.delete_instance()
        return "Dog Deletd"
    else:
        return False


def update_dog(data_dog):
    dog = Dog.filter(Dog.id == data_dog.id).first()
    if dog:
        for clave, valor in data_dog:
            if data_dog.id == valor or data_dog.id_user == valor:
                continue
            dog.update({clave:valor}).where(Dog.id == data_dog.id).execute()
        return "Dog Updated"
    
        
     
    
