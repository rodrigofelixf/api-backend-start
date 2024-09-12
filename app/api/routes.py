import logging
import time

from fastapi_cache.decorator import cache
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from redis.asyncio import Redis

from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine
from app.models import usuario_model
from app.models.schemas import schemas
from app.services import usuario_service

usuario_model.Base.metadata.create_all(bind=engine)


router = APIRouter()
endpointUsuario = "/usuarios/"

logging.basicConfig(level=logging.INFO)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






@router.post(endpointUsuario, response_model = schemas.Usuario)
def registrar_usuario(usuario: schemas.CriarUsuario, db: Session = Depends(get_db)):
    usuario_service.validar_usuario_existe(db, usuario.cpf, usuario.email)
    return usuario_service.criar_usuario(db, usuario)



@router.get(endpointUsuario, response_model=list[schemas.Usuario])
@cache(expire=1)
async def mostrar_lista_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    usuarios = await usuario_service.obter_todos_usuarios(db, skip, limit)

    return usuarios


@router.get(endpointUsuario + "buscarnome/{usuarioNome}", response_model=schemas.Usuario)
def buscar_usuario_por_nome(usuarioNome: str, db: Session = Depends(get_db)):
    usuarioEncontrado = usuario_service.obter_usuario_por_nome(db, usuarioNome)
    if usuarioEncontrado is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return usuarioEncontrado


@router.get(endpointUsuario + "{usuarioId}", response_model=schemas.Usuario)
def buscar_usuario_por_id(usuarioId: int, db: Session = Depends(get_db)):
    usuarioEncontrado = usuario_service.obter_usuario_por_id(db, usuarioId)
    if usuarioEncontrado is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return usuarioEncontrado

@router.get(endpointUsuario + "buscarusuarios/{usuarioNome}", response_model=list[schemas.Usuario])
def buscar_usuarios_pelo_nome(usuarioNome: str, db: Session = Depends(get_db)):
    usuariosEncontrados = usuario_service.obter_usuarios_pelo_nome(db, usuarioNome)
    if usuariosEncontrados is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return usuariosEncontrados


@router.get(endpointUsuario + "buscarcpf/{usuarioCpf}", response_model=schemas.Usuario)
def buscar_usuario_por_cpf(usuarioCpf: str, db: Session = Depends(get_db)):
    usuarioEncontrado = usuario_service.obter_usuario_por_cpf(db, usuarioCpf)
    if usuarioEncontrado is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return usuarioEncontrado


# @router.post("/prever/")
# async def prever_vulnerabilidade_social(dados: PacienteRequest):
#     resultado = prever_vulnerabilidade(dados)
#     return resultado



