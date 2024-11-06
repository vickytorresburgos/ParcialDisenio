import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.exc import OperationalError

from controllers.mutant_controller import router as mutant_router
from controllers.mutant_controller import MutantController
from config.database import Database

class InstanceNotFoundError(Exception):
    pass

def create_fastapi_app():
    app = FastAPI() # instancia de FastAPI

    @app.exception_handler(InstanceNotFoundError) # manejo de excepciones
    async def instance_not_found_exception_handler(request, exc):
        return JSONResponse(
            status_code=404,
            content={"message": str(exc)},
        )

    client_controller = MutantController() # instancia del controlador que maneja las rutas relacionadas con la deteccion de mutantes
    app.include_router(client_controller.router, prefix="/mutant")
    return app

def run_app(fastapi_app: FastAPI): # ejecucion del servidor
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    db = Database() # instancia de bd
    db.drop_database() # elimina por las dudas cualquier bd existente
    db.create_tables() # crea las tablas necesarias de la bd
    app = create_fastapi_app() # crea la aplicacion fastAPI
    run_app(app) # empieza a correr el servidor 