from fastapi import APIRouter, HTTPException # agrupar rutas relacionadas bajo un solo router
from pydantic import BaseModel # definir y validar los datos de entrada con clases
from services.dna_service import MutantService # logica de deteccion de mutantes y acceso a los datos
from repositories.dna_repository import DNARepository


class DnaRequest(BaseModel): # define el esquema de datos esperado para la secuencia de ADN en un POST
    dna: list[str]

class MutantController: 
    def __init__(self):
        self.router = APIRouter() # define y organiza las rutas
        self.repository = DNARepository() # instancia de capa de acceso a los datos
        self.setup_routes() # registra las rutas asociadas con detect_mutant y get_stats

    def setup_routes(self): # donfigura las rutas
        self.router.add_api_route("/", self.detect_mutant, methods=["POST"])
        self.router.add_api_route("/stats", self.get_stats, methods=["GET"])

    async def detect_mutant(self, dna_request: DnaRequest): # async define funciones asincronas // verifica si la secuencia es mutante
        
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
        
        # delega la logica de deteccion al servicio y el almacenamiento al repositorio

    async def get_stats(self): # devuelve estadisticas de la base de datos usando el repositorio
        stats = self.repository.get_stats()
        return stats

mutant_controller = MutantController()
router = mutant_controller.router # para importar el router directamente en la configuracion de FASTAPI