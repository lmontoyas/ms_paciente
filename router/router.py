from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from schema.paciente_schema import CrearPaciente
from schema.prueba_schema import CrearPrueba
from schema.resultado_triage_schema import CrearResultadoTriage
from schema.telefono_schema import CrearTelefono
from schema.triage_schema import CrearTriage
from model.paciente import paciente
from model.prueba import prueba
from model.triage import triage
from model.resultado_triage import resultado_triage
from model.telefono import telefono

pacientes = APIRouter()

@pacientes.get("/")
def root():
    return {"message": "Hi, I'm FastAPI with a router"}

# Paciente
@pacientes.post("/paciente")
def create_paciente(data_paciente: CrearPaciente, db: Session = Depends(get_db)):
    new_paciente = dict(data_paciente)
    try:
        db.execute(paciente.insert().values(new_paciente))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Paciente creado con éxito"}

@pacientes.get("/paciente/{historia}")
def read_paciente(historia: int, db: Session = Depends(get_db)):
    result = db.execute(paciente.select().where(paciente.c.historia == historia)).fetchone()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Paciente no encontrado")

@pacientes.put("/paciente/{historia}")
def update_paciente(historia: int, data_paciente: CrearPaciente, db: Session = Depends(get_db)):
    update_stmt = paciente.update().where(paciente.c.historia == historia).values(dict(data_paciente))
    result = db.execute(update_stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"message": "Paciente actualizado con éxito"}

@pacientes.get("/pacientes/")
def read_all_pacientes(db: Session = Depends(get_db)):
    results = db.execute(paciente.select()).fetchall()
    return results

# Prueba
@pacientes.post("/prueba")
def create_prueba(data_prueba: CrearPrueba, db: Session = Depends(get_db)):
    new_prueba = dict(data_prueba)
    try:
        db.execute(prueba.insert().values(new_prueba))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Prueba creada con éxito"}

@pacientes.get("/prueba/{id}")
def read_prueba(id: int, db: Session = Depends(get_db)):
    result = db.execute(prueba.select().where(prueba.c.id == id)).fetchone()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Prueba no encontrada")

@pacientes.put("/prueba/{id}")
def update_prueba(id: int, data_prueba: CrearPrueba, db: Session = Depends(get_db)):
    update_stmt = prueba.update().where(prueba.c.id == id).values(dict(data_prueba))
    result = db.execute(update_stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Prueba no encontrada")
    return {"message": "Prueba actualizada con éxito"}

@pacientes.get("/pruebas/")
def read_all_pruebas(db: Session = Depends(get_db)):
    results = db.execute(prueba.select()).fetchall()
    return results

# Resultado Triage
@pacientes.post("/resultado_triage")
def create_resultado_triage(data_resultado: CrearResultadoTriage, db: Session = Depends(get_db)):
    new_resultado = dict(data_resultado)
    try:
        db.execute(resultado_triage.insert().values(new_resultado))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Resultado de triage creado con éxito"}

@pacientes.get("/resultado_triage/{id}")
def read_resultado_triage(id: int, db: Session = Depends(get_db)):
    result = db.execute(resultado_triage.select().where(resultado_triage.c.id == id)).fetchone()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Resultado de triage no encontrado")

@pacientes.put("/resultado_triage/{id}")
def update_resultado_triage(id: int, data_resultado: CrearResultadoTriage, db: Session = Depends(get_db)):
    update_stmt = resultado_triage.update().where(resultado_triage.c.id == id).values(dict(data_resultado))
    result = db.execute(update_stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Resultado de triage no encontrado")
    return {"message": "Resultado de triage actualizado con éxito"}

@pacientes.get("/resultado_triages/")
def read_all_resultados_triage(db: Session = Depends(get_db)):
    results = db.execute(resultado_triage.select()).fetchall()
    return results

# Telefono
@pacientes.post("/telefono")
def create_telefono(data_telefono: CrearTelefono, db: Session = Depends(get_db)):
    new_telefono = dict(data_telefono)
    try:
        db.execute(telefono.insert().values(new_telefono))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Teléfono creado con éxito"}

@pacientes.get("/telefono/{numero}")
def read_telefono(numero: str, db: Session = Depends(get_db)):
    result = db.execute(telefono.select().where(telefono.c.numero == numero)).fetchone()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Teléfono no encontrado")

@pacientes.put("/telefono/{numero}")
def update_telefono(numero: str, data_telefono: CrearTelefono, db: Session = Depends(get_db)):
    update_stmt = telefono.update().where(telefono.c.numero == numero).values(dict(data_telefono))
    result = db.execute(update_stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Teléfono no encontrado")
    return {"message": "Teléfono actualizado con éxito"}

@pacientes.get("/telefonos/")
def read_all_telefonos(db: Session = Depends(get_db)):
    results = db.execute(telefono.select()).fetchall()
    return results

# Triage
@pacientes.post("/triage")
def create_triage(data_triage: CrearTriage, db: Session = Depends(get_db)):
    new_triage = dict(data_triage)
    try:
        db.execute(triage.insert().values(new_triage))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Triage creado con éxito"}

@pacientes.get("/triage/{id}")
def read_triage(id: int, db: Session = Depends(get_db)):
    result = db.execute(triage.select().where(triage.c.id == id)).fetchone()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Triage no encontrado")

@pacientes.put("/triage/{id}")
def update_triage(id: int, data_triage: CrearTriage, db: Session = Depends(get_db)):
    update_stmt = triage.update().where(triage.c.id == id).values(dict(data_triage))
    result = db.execute(update_stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Triage no encontrado")
    return {"message": "Triage actualizado con éxito"}

@pacientes.get("/triages/")
def read_all_triages(db: Session = Depends(get_db)):
    results = db.execute(triage.select()).fetchall()
    return results
