from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.dna_service import MutantService 
from repositories.dna_repository import DNARepository


class DnaRequest(BaseModel):
    dna: list[str]

class MutantController:
    def __init__(self):
        self.router = APIRouter()
        self.repository = DNARepository()
        self.setup_routes()

    def setup_routes(self):
        self.router.add_api_route("/", self.detect_mutant, methods=["POST"])
        self.router.add_api_route("/stats", self.get_stats, methods=["GET"])

    async def detect_mutant(self, dna_request: DnaRequest):
        dna = dna_request.dna

        if not dna:
            raise HTTPException(status_code=400, detail="Se requiere una secuencia de ADN")

        mutant_service = MutantService()
        if mutant_service.is_mutant(dna):  
            self.repository.save_dna(dna, is_mutant=True)
            return {"status": "Mutante detectado"}
        else:
            self.repository.save_dna(dna, is_mutant=False)
            raise HTTPException(status_code=403, detail="Humano detectado")

    async def get_stats(self):
        stats = self.repository.get_stats()
        return stats

mutant_controller = MutantController()
router = mutant_controller.router