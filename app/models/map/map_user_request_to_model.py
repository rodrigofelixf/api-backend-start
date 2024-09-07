from app.models.map import User_map
from app.models.request import User_Request

def map_request_to_model(user_request: UserRequest) -> Mapeamento:
    return Mapeamento(
        nome=user_request.nome,
        sexo=user_request.sexo,
        faixa_etaria=user_request.faixa_etaria,
        idade=user_request.idade,
        raca_cor=user_request.raca_cor,
        grupo=user_request.grupo,
        renda=user_request.renda,
        estado=user_request.estado,
        escolaridade=user_request.escolaridade,
        endereco=user_request.endereco,
        numero=user_request.numero,
        bairro=user_request.bairro,
        cidade=user_request.cidade,
        uf=user_request.uf,
        cep=user_request.cep,
        n_moradores=user_request.n_moradores
    )