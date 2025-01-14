from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta_data, engine

prueba = Table("prueba", meta_data,
    Column("id", Integer, primary_key = True, autoincrement=True),
    Column("descripcion", String(255), nullable = False),
)

meta_data.create_all(engine)
