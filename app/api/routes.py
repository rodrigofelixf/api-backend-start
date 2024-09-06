from fastapi import APIRouter

from app.models.requests.User_Request import UserRequest
from app.services.Vulnerabilidade_Service import prever_vulnerabilidade


router = APIRouter()

@router.post("/prever/")
async def prever_vulnerabilidade_social(dados: UserRequest):
    resultado = prever_vulnerabilidade(dados)
    return resultado



