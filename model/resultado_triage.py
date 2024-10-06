from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float
from config.db import meta_data, engine

resultado_triage = Table("resultado_triage", meta_data,
    Column("id", Integer, primary_key = True, autoincrement=True),
    Column("triage", Integer, ForeignKey('triage.id')),
    Column("prueba", Integer, ForeignKey('prueba.id')),
    Column("resultado", Float, nullable = False),
)

meta_data.create_all(engine)
