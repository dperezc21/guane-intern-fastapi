from models import Dog, User


def create_user(id_:str, name_:str, last_name_:str, email_:str):
    user = User.create(
        id = id_,
        name = name_,
        last_name = last_name_,
        email = email_
    )
    if user:
        return "user cretaed"
    else:
        return False


def get_user(id:str):
    user = User.select().where(User.id == id).first()
    return user


def delete_user(id:str):
    delete_user = User.select().where(User.id == id).first()
    dog = Dog.select().where(Dog.id_user == id).first()
    if not dog:
        delete_user.delete_instance()
        return "User Deleted"
    elif delete_user:
        dog.delete_instance()
        delete_user.delete_instance()
        return "User Deletd"
    else:
        return False


def update_user_(data_user):
    user = User.filter(User.id == data_user.id).first()
    if user:
        for clave, valor in data_user:
            if valor == data_user.id:
                continue
            user.update({clave:valor}).where(User.id == data_user.id).execute()
        
        return "user updated"