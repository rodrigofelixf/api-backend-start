from pydantic.v1 import BaseModel


class UserInput(BaseModel):
    nomeCompleto: str
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
