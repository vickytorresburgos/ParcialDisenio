from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import declarative_base

base = declarative_base() # clase base que la heredan todos los modelos -> DNAModel representa una tabla en la bd

class DNAModel(base): # define estructura de la tabla dna 
    __tablename__ = 'dna'
    
    id = Column(Integer, primary_key=True, index=True)
    dna = Column(String(255), unique=True, nullable=False) 
    is_mutant = Column(Boolean, nullable=False)

# facilita la interaccion con la base de datos para operaciones CRUD