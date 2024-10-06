from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Date
from config.db import meta_data, engine

triage = Table("triage", meta_data,
    Column("id", Integer, primary_key = True, autoincrement=True),
    Column("historia", Integer, ForeignKey('paciente.historia')),
    Column("fecha", Date, nullable = False),
)

meta_data.create_all(engine)

