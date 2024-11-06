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
    app = FastAPI()

    @app.exception_handler(InstanceNotFoundError)
    async def instance_not_found_exception_handler(request, exc):
        return JSONResponse(
            status_code=404,
            content={"message": str(exc)},
        )

    client_controller = MutantController()
    app.include_router(client_controller.router, prefix="/mutant")
    return app

def run_app(fastapi_app: FastAPI):
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    db = Database()
    db.drop_database()
    db.create_tables()
    app = create_fastapi_app()
    run_app(app)