from sqlalchemy import Integer, Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta_data, engine

telefono = Table("telefono", meta_data,
    Column("numero", String(9), primary_key = True),
    Column("historia", Integer, ForeignKey('paciente.historia')),
)

meta_data.create_all(engine)

