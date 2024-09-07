from sqlalchemy.orm import Session
from app.models.Paciente_Model import PacienteModel
from app.models.requests.Paciente_Dto import PacienteDto
from app.models.requests.Paciente_Request import PacienteRequest


async def criar_paciente(db: Session, pacientedto: PacienteDto):
    db_paciente = PacienteModel(**pacientedto.model_dump())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente
