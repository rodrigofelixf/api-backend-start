from sqlalchemy import Column, String, Integer, Float, Boolean, Date
from app.db.database import Base

class UsuarioModel(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)  # Índice na coluna 'id'
    nomeCompleto = Column(String, nullable=False, index=True)  # Índice na coluna 'nomeCompleto'
    email = Column(String, nullable=False, unique=True, index=True)  # Índice único na coluna 'email'
    cpf = Column(String, nullable=False, unique=True, index=True)  # Índice único na coluna 'cpf'
    dataNascimento = Column(Date, nullable=False)
    sexo = Column(String, nullable=False)
    rg = Column(String, nullable=True)
    idade = Column(Integer, nullable=False)
    nomeMae = Column(String, nullable=False)
    telefone = Column(String, nullable=True)
    cep = Column(Integer, nullable=False)
    cidade = Column(String, nullable=False)
    rua = Column(String, nullable=False)
    uf = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    numeroEndereco = Column(Integer, nullable=True)
    escolaridade = Column(String, nullable=False)
    racaCor = Column(String, nullable=False)
    faixaEtaria = Column(String, nullable=False)
    estadoCivil = Column(String, nullable=False)
    pcd = Column(Boolean, nullable=False)
    tipoPcd = Column(String, nullable=True)
    cursoSuperior = Column(String, nullable=True)
    renda = Column(Float, nullable=False)
    emprego = Column(String, nullable=True)
    numeroMoradores = Column(Integer, nullable=False)
    grupo = Column(String, nullable=False)
    isVulneravel = Column(Boolean, default=False)

    # Se precisar adicionar índices compostos, você pode usar Index
    # from sqlalchemy import Index
    # __table_args__ = (
    #     Index('ix_user_name_email', 'nomeCompleto', 'email'),
    # )
