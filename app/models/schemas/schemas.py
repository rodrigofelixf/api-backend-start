from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioBase(BaseModel):
    email: str



class CriarUsuario(UsuarioBase):
    nomeCompleto: str
    email: str
    cpf: str
    dataNascimento: date
    sexo: str
    rg: Optional[str] = None
    idade: int
    nomeMae: str
    telefone: Optional[str] = None
    cep: int
    cidade: str
    rua: str
    uf: str
    bairro: str
    numeroEndereco: Optional[int] = None
    escolaridade: str
    racaCor: str
    faixaEtaria: str
    estadoCivil: str
    pcd: bool
    tipoPcd: Optional[str] = None
    cursoSuperior: Optional[str] = None
    renda: float
    emprego: Optional[str] = None
    numeroMoradores: int
    grupo: str


class Usuario(UsuarioBase):
    id: int
    isVulneravel: bool

class Config:
    orm_mode = True



