from pydantic import BaseModel

class CrearTelefono(BaseModel):
    numero: str
    historia: int
