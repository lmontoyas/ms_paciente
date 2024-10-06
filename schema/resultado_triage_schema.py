from pydantic import BaseModel

class CrearResultadoTriage(BaseModel):
    triage: int
    prueba: int
    resultado: float
