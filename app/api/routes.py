from fastapi import APIRouter

from app.models.requests.Paciente_Request import PacienteRequest
from app.services.Vulnerabilidade_Service import prever_vulnerabilidade

from app.db.database import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/prever/")
async def prever_vulnerabilidade_social(dados: PacienteRequest):
    resultado = prever_vulnerabilidade(dados)
    return resultado



