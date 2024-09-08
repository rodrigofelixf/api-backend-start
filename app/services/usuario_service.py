from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import usuario_model
from app.models.schemas import schemas
from app.services.vulnerabilidade_service import prever_vulnerabilidade


def obter_usuario_por_id(db: Session, usuario_id: int):
    usuario = db.query(usuario_model.UsuarioModel).filter(usuario_model.UsuarioModel.id == usuario_id).first()
    return usuario

def obter_usuario_por_nome(db: Session, usuario_nome: str):
    usuario = db.query(usuario_model.UsuarioModel).filter(usuario_model.UsuarioModel.nomeCompleto.ilike(f"%{usuario_nome}")).first()
    return usuario

def obter_usuarios_pelo_nome(db: Session, usuario_nome: str):
    usuario = db.query(usuario_model.UsuarioModel).filter(usuario_model.UsuarioModel.nomeCompleto.ilike(f"%{usuario_nome}")).all()
    return usuario

def obter_usuario_por_cpf(db: Session, usuario_cpf: str):
    usuario = db.query(usuario_model.UsuarioModel).filter(usuario_model.UsuarioModel.cpf == usuario_cpf).first()
    return usuario

def obter_usuario_por_email(db: Session, usuario_email: str):
    usuario = db.query(usuario_model.UsuarioModel).filter(usuario_model.UsuarioModel.email == usuario_email).first()
    return usuario

def obter_todos_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(usuario_model.UsuarioModel).offset(skip).limit(limit).all()


def criar_usuario(db: Session, usuario: schemas.CriarUsuario):
    is_vulneravel = prever_vulnerabilidade(usuario)

    usuario_dados = usuario.model_dump()
    usuario_dados['isVulneravel'] = is_vulneravel

    usuario_para_salvar = usuario_model.UsuarioModel(**usuario_dados)

    db.add(usuario_para_salvar)
    db.commit()
    db.refresh(usuario_para_salvar)

    return usuario_para_salvar



def validar_usuario_existe(db: Session, cpf: str, email: str):
    if obter_usuario_por_cpf(db, cpf):
        raise HTTPException(status_code=400, detail="CPF já cadastrado!")
    if obter_usuario_por_email(db, email):
        raise HTTPException(status_code=400, detail="E-mail já cadastrado!")
