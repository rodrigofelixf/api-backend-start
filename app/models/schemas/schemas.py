from pydantic import BaseModel
from typing import Optional
from datetime import date

from app.models.enums import Sexo, FaixaEtaria, RacaCor, Grupo, EstadoCivil, Escolaridade, Cidade


class CriarUsuario(BaseModel):
    nomeCompleto: str
    email: str
    cpf: str
    dataNascimento: date
    sexo: Sexo
    rg: Optional[str] = None
    idade: int
    nomeMae: str
    telefone: Optional[str] = None
    cep: int
    cidade: Cidade
    rua: str
    uf: str
    bairro: str
    numeroEndereco: Optional[int] = None
    escolaridade: Escolaridade
    racaCor: RacaCor
    faixaEtaria: FaixaEtaria
    estadoCivil: EstadoCivil
    pcd: bool
    tipoPcd: Optional[str] = None
    cursoSuperior: Optional[str] = None
    renda: float
    emprego: Optional[str] = None
    numeroMoradores: int
    grupo: Grupo

class Usuario(BaseModel):
    cpf: str
    nomeCompleto: str
    email: str
    isVulneravel: bool

class Config:
    orm_mode = True


class VulnerabilidadeDadosTreino(BaseModel):
    nome: str
    sexo: str  # Alterado para str para simplificar a conversão, ajuste conforme necessidade
    faixa_etaria: str
    idade: int
    raca_cor: str
    grupo: str
    renda: float
    estado: str
    escolaridade: str
    endereco: str
    numero: int
    bairro: str
    cidade: str
    uf: str
    cep: int
    n_moradores: int
