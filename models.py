
from peewee import *
from database import db


class User(Model):
    id = CharField(max_length=10)
    name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    email = CharField(max_length=20)

    class Meta:
        database = db


class Dog(Model):
    id = CharField(max_length=10)
    name = CharField(max_length=20)
    pinture = CharField()
    is_adopted = BooleanField()
    create_date = DateTimeField()
    id_user = CharField(max_length=10)

    class Meta:
        database = db
    
    
    