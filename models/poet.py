from pydantic import BaseModel

class Poet(BaseModel):
    name: str
    avatar: str
    birthdate: str
    country: str
