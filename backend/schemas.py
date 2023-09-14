#schemas.py

from pydantic import BaseModel

# Estas clases son esquemas para usar mas adelante, NO son tablas de la bsae de datos
class UserData(BaseModel):
    name : str
    password: str


class UserId(UserData):
    id: int
