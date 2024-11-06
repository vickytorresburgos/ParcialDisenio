from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import declarative_base

base = declarative_base()

class DNAModel(base):
    __tablename__ = 'dna'
    
    id = Column(Integer, primary_key=True, index=True)
    dna = Column(String(255), unique=True, nullable=False) 
    is_mutant = Column(Boolean, nullable=False)