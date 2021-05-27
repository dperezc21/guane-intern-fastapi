
from peewee import *
from database import db


class User(Model):
    id = PrimaryKeyField()
    name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    email = CharField(max_length=20)

    class Meta:
        database = db


class Dog(Model):
    id = PrimaryKeyField()
    name = CharField(max_length=20)
    pinture = CharField()
    is_adopted = BooleanField()
    create_date = DateTimeField()
    id_user = ForeignKeyField(User, backref="dogs")

    class Meta:
        database = db
    
    
    