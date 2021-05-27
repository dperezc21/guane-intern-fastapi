from models import User


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
    user_deleted = User.select().where(User.id == id).first()
    if user_deleted:
        user_deleted.delete_instance()
        return "Dog Deletd"
    else:
        return False

