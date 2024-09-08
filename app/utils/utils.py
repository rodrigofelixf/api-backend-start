# from app.models.schemas import schemas
#
# usuario = schemas.CriarUsuario()
#
# usuario_data = {
#     'nomeCompleto': usuario.nomeCompleto,
#     'email': usuario.email,
#     'cpf': usuario.cpf,
#     'dataNascimento': usuario.data_nascimento,
#     'sexo': usuario.sexo,
#     'rg': usuario.rg,
#     'idade': usuario.idade,
#     'nomeMae': usuario.nome_mae,
#     'telefone': usuario.telefone,
#     'cep': usuario.cep,
#     'cidade': usuario.cidade,
#     'rua': usuario.rua,
#     'uf': usuario.uf,
#     'bairro': usuario.bairro,
#     'numeroEndereco': usuario.numero_endereco,
#     'escolaridade': usuario.escolaridade,
#     'racaCor': usuario.raca_cor,
#     'faixaEtaria': usuario.faixa_etaria,
#     'estadoCivil': usuario.estado_civil,
#     'pcd': usuario.pcd,
#     'tipoPcd': usuario.tipo_pcd,
#     'cursoSuperior': usuario.curso_superior,
#     'renda': usuario.renda,
#     'emprego': usuario.emprego,
#     'numeroMoradores': usuario.numero_moradores,
#     'grupo': usuario.grupo
# }
#

from app.models.schemas import schemas
from app.models.schemas.schemas import CriarUsuario, VulnerabilidadeDadosTreino


def converter_para_paciente_request(dados_usuario: CriarUsuario) -> VulnerabilidadeDadosTreino:
    return VulnerabilidadeDadosTreino(
        nome=dados_usuario.nomeCompleto,
        sexo=dados_usuario.sexo,
        faixa_etaria=dados_usuario.faixaEtaria,
        idade=dados_usuario.idade,
        raca_cor=dados_usuario.racaCor,
        grupo=dados_usuario.grupo,
        renda=dados_usuario.renda,
        estado=dados_usuario.estadoCivil,
        escolaridade=dados_usuario.escolaridade,
        endereco=dados_usuario.rua,
        numero=dados_usuario.numeroEndereco if dados_usuario.numeroEndereco else 0,  # Ajuste para o valor padrão
        bairro=dados_usuario.bairro,
        cidade=dados_usuario.cidade,
        uf=dados_usuario.uf,
        cep=dados_usuario.cep,
        n_moradores=dados_usuario.numeroMoradores
    )
