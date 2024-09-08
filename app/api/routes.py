from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine
from app.models import usuario_model
from app.models.schemas import schemas
from app.services import usuario_service

usuario_model.Base.metadata.create_all(bind=engine)


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/usuarios/", response_model = schemas.Usuario)
def registrar_usuario(usuario: schemas.CriarUsuario, db: Session = Depends(get_db)):
    usuario_service.validar_usuario_existe(db, usuario.cpf, usuario.email)
    return usuario_service.criar_usuario(db, usuario)


@router.get("/usuarios/", response_model=list[schemas.Usuario])
def mostrar_lista_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = usuario_service.obter_todos_usuarios(db, skip, limit)
    return usuarios


@router.get("/usuarios/{usuarioId}", response_model=schemas.Usuario)
def buscar_usuario_por_id(usuarioId: int, db: Session = Depends(get_db)):
    usuarioEncontrado = usuario_service.obter_usuario_por_id(db, usuarioId)
    if usuarioEncontrado is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return usuarioEncontrado


# @router.post("/prever/")
# async def prever_vulnerabilidade_social(dados: PacienteRequest):
#     resultado = prever_vulnerabilidade(dados)
#     return resultado



