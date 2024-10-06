from fastapi import FastAPI
from router.router import pacientes 

app = FastAPI()

app.include_router(pacientes)

