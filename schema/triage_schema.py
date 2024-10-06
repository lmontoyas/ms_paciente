from pydantic import BaseModel
from datetime import date

class CrearTriage(BaseModel):
    historia: int
    fecha: date
