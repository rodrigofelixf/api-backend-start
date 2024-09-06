from pydantic import BaseModel

from app.models.enums import Sexo, FaixaEtaria, RacaCor, Grupo, EstadoCivil, Escolaridade, Cidade, Uf


class UserRequest(BaseModel):
    nome: str
    sexo: Sexo
    faixa_etaria: FaixaEtaria
    idade: int
    raca_cor: RacaCor
    grupo: Grupo
    renda: float
    estado: EstadoCivil
    escolaridade: Escolaridade
    endereco: str
    numero: int
    bairro: str
    cidade: Cidade
    uf: Uf
    cep: int
    n_moradores: int