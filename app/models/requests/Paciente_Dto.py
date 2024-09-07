from pydantic import BaseModel
from typing import Optional

class PacienteDto(BaseModel):
    nomeCompleto: str
    email: str
    sexo: str
    faixaEtaria: str
    idade: int
    racaCor: str
    grupo: str
    renda: float
    estadoCivil: str
    escolaridade: str
    endereco: str
    numeroCasa: int
    bairro: str
    cidade: str
    uf: str
    cep: str
    numeroMoradores: int
    vulneravel: bool
