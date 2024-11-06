from sqlalchemy.orm import Session # contexto de la sesion para operaciones de base de datos
from models.dna import DNAModel # modelo que representa la tabla dna
from config.database import Database # gestion de conexion con la base de datos

class DNARepository:
    def __init__(self):
        self.db = Database() #instancia de Database para obtener sesiones de la base de datos

    def save_dna(self, dna, is_mutant): # guarda una secuencia de ADN en la bd
        dna = ''.join(dna) # convierte la lista en una cadena
        with self.db.get_session() as session: # abre una sesion para realizar la operacion de bd
            new_dna = DNAModel(dna=dna, is_mutant=is_mutant) # crea un adn con la secuencia de adn y su estado
            session.add(new_dna) # agrega el objeto a la sesion actual
            session.commit() # guarda los cambios en la bd

    def get_stats(self): # obtiene estadisticas sobre el adn mutante y humano almacenado
        with self.db.get_session() as session:
            mutant_dna = session.query(DNAModel).filter_by(is_mutant=True).count()
            human_dna = session.query(DNAModel).filter_by(is_mutant=False).count()
            total_dna = mutant_dna + human_dna
            ratio = mutant_dna / total_dna if total_dna > 0 else 0
            return {
                "ADN Mutante": mutant_dna,
                "ADN Humano": human_dna,
                "ratio": ratio
            }