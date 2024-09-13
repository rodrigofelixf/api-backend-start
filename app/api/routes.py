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

@router.get(endpointUsuario + "buscarusuarioscpf/{cpf}", response_model=list[schemas.Usuario])
def buscar_usuarios_pelo_cpf(cpf: str, db: Session = Depends(get_db)):
    usuariosEncontrados = usuario_service.obter_usuarios_pelo_cpf(db, cpf)
    if usuariosEncontrados is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return usuariosEncontrados


@router.get(endpointUsuario + "buscarcpf/{usuarioCpf}", response_model=schemas.Usuario)
def buscar_usuario_por_cpf(usuarioCpf: str, db: Session = Depends(get_db)):
    usuarioEncontrado = usuario_service.obter_usuario_por_cpf(db, usuarioCpf)
    if usuarioEncontrado is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return usuarioEncontrado


@router.post("/upload-csv/")
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

    # Garantir que 'cep' é tratado como string
    dataframe['cep'] = dataframe['cep'].astype(str)

    usuarios_criados = []
    usuarios_existentes = set()

    for _, row in dataframe.iterrows():
        # Verificar e corrigir o formato dos dados
        try:
            usuario_data = schemas.CriarUsuario(
                nomeCompleto=row.get("nomeCompleto", ""),
                email=row.get("email", ""),
                cpf=row.get("cpf", ""),
                dataNascimento=row.get("dataNascimento", ""),
                sexo=row.get("sexo", ""),
                rg=row.get("rg"),
                idade=row.get("idade", 0),
                nomeMae=row.get("nomeMae", ""),
                telefone=row.get("telefone"),
                cep=row.get("cep", ""),  # Mantém `cep` como string
                cidade=row.get("cidade", ""),
                rua=row.get("rua", ""),
                uf=row.get("uf", ""),
                bairro=row.get("bairro", ""),
                numeroEndereco=row.get("numeroEndereco"),
                escolaridade=row.get("escolaridade", ""),
                racaCor=row.get("racaCor", ""),
                faixaEtaria=row.get("faixaEtaria", ""),
                estadoCivil=row.get("estadoCivil", ""),
                pcd=bool(row.get("pcd", False)),  # Verifica se `pcd` é booleano
                tipoPcd=row.get("tipoPcd"),
                cursoSuperior=row.get("cursoSuperior"),
                renda=float(row.get("renda", 0.0)),  # Verifica se `renda` é float
                emprego=row.get("emprego"),
                numeroMoradores=row.get("numeroMoradores", 0),
                grupo=row.get("grupo", "")
            )
        except ValueError as e:
            logger.error(f"Erro ao processar a linha {row}: {e}")
            continue  # Ignora linhas com erro e continua com o próximo usuário

        try:
            usuario_service.validar_usuario_existe(db, usuario_data.cpf, usuario_data.email)
            usuario_criado = usuario_service.criar_usuario(db, usuario_data)
            usuarios_criados.append(usuario_criado)
            usuarios_existentes.add(usuario_data.email)
        except HTTPException as e:
            logger.error(f"Erro ao criar usuário com email {usuario_data.email}: {e.detail}")
            continue

    return {"message": f"{len(usuarios_criados)} usuários foram criados com sucesso!"}


@router.get(endpointUsuario + "filtro/vulneraveis", response_model=list[schemas.Usuario])
def buscar_usuarios_vulneraveis(db: Session = Depends(get_db)):
    usuarios_vulneraveis = usuario_service.obter_usuarios_vulneraveis(db)
    if not usuarios_vulneraveis:
        raise HTTPException(status_code=404, detail="Nenhum usuário vulnerável encontrado")
    return usuarios_vulneraveis


@router.get(endpointUsuario + "filtro/nao-vulneraveis", response_model=list[schemas.Usuario])
def buscar_usuarios_nao_vulneraveis(db: Session = Depends(get_db)):
    usuarios_nao_vulneraveis = usuario_service.obter_usuarios_nao_vulneraveis(db)
    if not usuarios_nao_vulneraveis:
        raise HTTPException(status_code=404, detail="Nenhum usuário não vulnerável encontrado")
    return usuarios_nao_vulneraveis







