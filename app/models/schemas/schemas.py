from datetime import date
from typing import Optional

from pydantic import field_validator
from pydantic import BaseModel
from pydantic.v1 import ConfigDict



class CriarUsuario(BaseModel):
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



class Usuario(BaseModel):
    cpf: str
    nomeCompleto: str
    email: str
    isVulneravel: bool

    # Validador para capitalizar o nome corretamente
    @field_validator('nomeCompleto', mode='before')
    def capitalizar_nome(cls, v):
        if v:
            return v.title()  # Capitaliza o nome
        return v

    # Atualize a configuração para o novo formato
    model_config = ConfigDict(
        from_attributes=True  # Substitui 'orm_mode'
    )

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


