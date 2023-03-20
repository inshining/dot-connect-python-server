from pydantic import BaseModel

class BrailleBody(BaseModel):
    braille: str

class BrailleResponse(BaseModel):
    str: str
    braille: list[int]
