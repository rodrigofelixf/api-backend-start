from sqlalchemy import Column, String, Integer, Float, Boolean, Date, Enum
from app.db.database import Base
from app.models.enums import Sexo, Cidade, Escolaridade, RacaCor, FaixaEtaria, EstadoCivil, Grupo


class UsuarioModel(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)  # Índice na coluna 'id'
    nomeCompleto = Column(String, nullable=False, index=True)  # Índice na coluna 'nomeCompleto'
    email = Column(String, nullable=False, unique=True, index=True)  # Índice único na coluna 'email'
    cpf = Column(String, nullable=False, unique=True, index=True)  # Índice único na coluna 'cpf'
    dataNascimento = Column(Date, nullable=False)
    sexo = Column(Enum(Sexo), nullable=False)  # Enum para o campo sexo
    rg = Column(String, nullable=True)
    idade = Column(Integer, nullable=False)
    nomeMae = Column(String, nullable=False)
    telefone = Column(String, nullable=True)
    cep = Column(Integer, nullable=False)
    cidade = Column(Enum(Cidade), nullable=False)  # Enum para o campo cidade
    rua = Column(String, nullable=False)
    uf = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    numeroEndereco = Column(Integer, nullable=True)
    escolaridade = Column(Enum(Escolaridade), nullable=False)  # Enum para o campo escolaridade
    racaCor = Column(Enum(RacaCor), nullable=False)  # Enum para o campo racaCor
    faixaEtaria = Column(Enum(FaixaEtaria), nullable=False)  # Enum para o campo faixaEtaria
    estadoCivil = Column(Enum(EstadoCivil), nullable=False)  # Enum para o campo estadoCivil
    pcd = Column(Boolean, nullable=False)
    tipoPcd = Column(String, nullable=True)
    cursoSuperior = Column(String, nullable=True)
    renda = Column(Float, nullable=False)
    emprego = Column(String, nullable=True)
    numeroMoradores = Column(Integer, nullable=False)
    grupo = Column(Enum(Grupo), nullable=False)  # Enum para o campo grupo
    isVulneravel = Column(Boolean, default=False)
