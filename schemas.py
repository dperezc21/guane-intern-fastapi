from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ModelDogs(BaseModel):
    id : Optional[str]
    name: str
    pinture: Optional[str]
    is_adopted: Optional[bool]
    create_date: Optional[datetime]


class ModelUser(BaseModel):
    id:str
    name:str
    last_name:str
    email:str



    
