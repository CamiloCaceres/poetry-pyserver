from pydantic import BaseModel

class Poem(BaseModel):
    title: str
    text: str
    poet: str