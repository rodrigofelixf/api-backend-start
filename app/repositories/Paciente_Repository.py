from sqlalchemy.orm import Session
from app.models.usuario_model import UsuarioModel
from app.models.requests.Paciente_Dto import PacienteDto
from app.models.requests.Paciente_Request import PacienteRequest


async def criar_paciente(db: Session, pacientedto: PacienteDto):
    db_paciente = UsuarioModel(**pacientedto.model_dump())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente
