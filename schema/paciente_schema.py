from pydantic import BaseModel
from datetime import date

class CrearPaciente(BaseModel):
    tipo_doc: str
    num_doc: int
    nombre_apellido: str
    fecha_nac: date
    estado_civil: str
    pais_nac: str
    direccion: str
    sexo: str
