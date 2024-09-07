
from app.db.database import Base

from sqlalchemy import Column, String, Integer, Float, Boolean


class PacienteModel(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)  #
    nomeCompleto = Column(String, nullable=False)
    sexo = Column(String, nullable=False)
    faixaEtaria = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    racaCor = Column(String, nullable=False)
    grupo = Column(String, nullable=False)
    renda = Column(Float, nullable=False)
    estadoCivil = Column(String, nullable=False)
    escolaridade = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    numeroCasa = Column(Integer, nullable=False)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    uf = Column(String, nullable=False)
    cep = Column(Integer, nullable=False)
    numeroMoradores = Column(Integer, nullable=False)
    vulneravel = Column(Boolean, default=False)
