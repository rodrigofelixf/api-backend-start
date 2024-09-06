

from enum import Enum

class Sexo(Enum):
    feminino = "feminino"
    masculino = "masculino"

class FaixaEtaria(Enum):
    de_0_a_19 = "0 a 19 anos"
    de_20_a_24 = "20 a 24 anos"
    de_25_a_29 = "25 a 29 anos"
    de_30_a_34 = "30 a 34 anos"
    de_35_a_39 = "35 a 39 anos"
    de_40_a_44 = "40 a 44 anos"
    de_45_a_49 = "45 a 49 anos"
    de_50_a_54 = "50 a 54 anos"
    de_55_a_59 = "55 a 59 anos"
    de_60_a_64 = "60 a 64 anos"
    de_65_a_69 = "65 a 69 anos"
    de_70_a_74 = "70 a 74 anos"
    de_75_a_79 = "75 a 79 anos"
    de_80_a_84 = "80 a 84 anos"
    de_85_a_89 = "85 a 89 anos"
    de_90_a_94 = "90 a 94 anos"
    de_95_a_99 = "95 a 99 anos"
    acima_100 = "100 anos +"

class RacaCor(Enum):
    amarela = "amarela"
    branca = "branca"
    indigena = "indigena"
    parda = "parda"
    preta = "preta"

class Grupo(Enum):
    caminhoneiros = "caminhoneiros"
    gestantes_e_puerperas = "gestantes e puerperas"
    gestantes_e_puerperas_nao_residentes_em_recife = "gestantes e puerperas nao residentes em recife"
    pessoas_com_comorbidades = "pessoas com comorbidades"
    pessoas_com_viagem_para_exterior = "pessoas com viagem para exterior (estudo/pesquisa/trabalho/tratamento de saude)"
    pessoas_em_situacao_de_rua = "pessoas em situacao de rua"
    publico_em_geral = "publico em geral (18 a 59 anos)"
    trabalhadores_da_assistencia_social = "trabalhadores da assistencia social"
    trabalhadores_da_educacao = "trabalhadores da educacao"
    trabalhadores_da_saude = "trabalhadores da saude"
    trabalhadores_de_transporte_aereo = "trabalhadores de transporte aereo"
    trabalhadores_de_transporte_aquaviario = "trabalhadores de transporte aquaviario"
    trabalhadores_de_transporte_coletivo_rodoviario = "trabalhadores de transporte coletivo rodoviario"
    trabalhadores_de_transporte_metroviario_e_ferroviario = "trabalhadores de transporte metroviario e ferroviario"
    trabalhadores_industriais_e_bancarios = "trabalhadores industriais e bancarios"
    trabalhadores_portuarios = "trabalhadores portuarios"
    trabalhadores_da_limpeza_urbana = "trabalhadores da limpeza urbana"
    sesau_busca_ativa = "sesau - busca ativa"
    outras_prioridades = "outras prioridades"

class EstadoCivil(Enum):
    casado = "casado"
    divorciado = "divorciado"
    solteiro = "solteiro"
    viuvo = "viuvo"

class Escolaridade(Enum):
    curso_tecnico_tecnologo = "curso tecnico / tecnologo"
    ensino_medio_completo = "ensino medio completo"
    ensino_superior_completo = "ensino superior completo"

class Cidade(Enum):
    abreu_e_lima = "abreu e lima"
    barreiros = "barreiros"
    cabo_de_santo_agostinho = "cabo de santo agostinho"
    camaragibe = "camaragibe"
    caruaru = "caruaru"
    igarassu = "igarassu"
    ipojuca = "ipojuca"
    jaboatao_dos_guararapes = "jaboatao dos guararapes"
    morro_da_conceicao = "morro da conceicao"
    olinda = "olinda"
    paulista = "paulista"
    recife = "recife"

class Uf(Enum):
    pe = "pe"
