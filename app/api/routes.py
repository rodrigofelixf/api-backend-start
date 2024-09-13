import logging
from io import StringIO

import pandas as pd
from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.params import Depends, File
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine
from app.models import usuario_model
from app.models.schemas import schemas
from app.services import usuario_service

usuario_model.Base.metadata.create_all(bind=engine)


router = APIRouter()
endpointUsuario = "/usuarios/"


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



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


@router.post(endpointUsuario + "upload-csv/")
async def carregar_arquivo_csv_cadastrar_usuarios(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="O arquivo precisa ser um CSV.")

    contents = await file.read()
    csv_data = StringIO(contents.decode("utf-8"))
    dataframe = pd.read_csv(csv_data)

    required_columns = [
        "nomeCompleto", "email", "cpf", "dataNascimento", "sexo", "rg", "idade", "nomeMae",
        "telefone", "cep", "cidade", "rua", "uf", "bairro", "numeroEndereco", "escolaridade",
        "racaCor", "faixaEtaria", "estadoCivil", "pcd", "tipoPcd", "cursoSuperior",
        "renda", "emprego", "numeroMoradores", "grupo"
    ]

    if not all(col in dataframe.columns for col in required_columns):
        raise HTTPException(status_code=400, detail="O CSV não contém todas as colunas necessárias.")

    usuarios_criados = []
    usuarios_existentes = set()

    for _, row in dataframe.iterrows():
        # Verificar se o e-mail já está cadastrado
        if row["email"] in usuarios_existentes:
            continue  # Pular este registro se o e-mail já foi processado

        usuario_data = schemas.CriarUsuario(
            nomeCompleto=row["nomeCompleto"],
            email=row["email"],
            cpf=row["cpf"],
            dataNascimento=row["dataNascimento"],
            sexo=row["sexo"],
            rg=row.get("rg"),
            idade=row["idade"],
            nomeMae=row["nomeMae"],
            telefone=row.get("telefone"),
            cep=row["cep"],
            cidade=row["cidade"],
            rua=row["rua"],
            uf=row["uf"],
            bairro=row["bairro"],
            numeroEndereco=row.get("numeroEndereco"),
            escolaridade=row["escolaridade"],
            racaCor=row["racaCor"],
            faixaEtaria=row["faixaEtaria"],
            estadoCivil=row["estadoCivil"],
            pcd=row["pcd"],
            tipoPcd=row.get("tipoPcd"),
            cursoSuperior=row.get("cursoSuperior"),
            renda=row["renda"],
            emprego=row.get("emprego"),
            numeroMoradores=row["numeroMoradores"],
            grupo=row["grupo"]
        )

        try:
            usuario_service.validar_usuario_existe(db, usuario_data.cpf, usuario_data.email)
            usuario_criado = usuario_service.criar_usuario(db, usuario_data)
            usuarios_criados.append(usuario_criado)
            usuarios_existentes.add(usuario_data.email)  # Adiciona o e-mail à lista de processados
        except HTTPException as e:
            logger.error(f"Erro ao criar usuário com email {usuario_data.email}: {e.detail}")
            continue  # Ignora o erro e continua com o próximo usuário

    return {"message": f"{len(usuarios_criados)} usuários foram criados com sucesso!"}







