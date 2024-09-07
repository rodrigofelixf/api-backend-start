from sqlalchemy.orm import Session

from app.models.requests.Paciente_Dto import PacienteDto
from app.repositories.Paciente_Repository import criar_paciente


def registrar_paciente(db: Session, pacientedto: PacienteDto):
    return  criar_paciente(db, pacientedto)