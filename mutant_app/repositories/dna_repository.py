from sqlalchemy.orm import Session
from models.dna import DNAModel
from config.database import Database

class DNARepository:
    def __init__(self):
        self.db = Database()

    def save_dna(self, dna, is_mutant):
        dna = ''.join(dna)
        with self.db.get_session() as session:
            new_dna = DNAModel(dna=dna, is_mutant=is_mutant)
            session.add(new_dna)
            session.commit()

    def get_stats(self):
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