from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta_data, engine

paciente = Table("paciente", meta_data,
    Column("historia", Integer, primary_key = True, autoincrement=True),
    Column("tipo_doc", String(255), nullable = False),
    Column("num_doc", Integer, nullable = False),
    Column("nombre_apellido", String(255), nullable = False),
    Column("fecha_nac", Date, nullable = False),
    Column("estado_civil", String(255), nullable = False),
    Column("pais_nac", String(255), nullable = False),
    Column("direccion", String(255), nullable = False),
    Column("sexo", String(255), nullable = False),
)

meta_data.create_all(engine)

