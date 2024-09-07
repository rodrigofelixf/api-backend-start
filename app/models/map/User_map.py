class Mapeamento:
    def __init__(self, nome, sexo, faixa_etaria, idade, raca_cor, grupo, renda, estado, escolaridade, endereco, numero, bairro, cidade, uf, cep, n_moradores):
        self.nome = nomeCompleto
        self.sexo = sexo
        self.faixa_etaria =     faixaEtaria
        self.idade = idade
        self.raca_cor = racaCor
        self.grupo = grupo
        self.renda = renda
        self.estado = estadoCivil
        self.escolaridade = escolaridade
        self.endereco = endereco
        self.numero = numeroCasa
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.n_moradores = numeroMoradores

    def __repr__(self):
        return (f"Pessoa(nome={self.nome}, sexo={self.sexo}, faixa_etaria={self.faixa_etaria}, "
                f"idade={self.idade}, raca_cor={self.raca_cor}, grupo={self.grupo}, "
                f"renda={self.renda}, estado_civil={self.estado}, escolaridade={self.escolaridade}, "
                f"endereco={self.endereco}, numero={self.numero}, bairro={self.bairro}, "
                f"cidade={self.cidade}, uf={self.uf}, cep={self.cep}, numero_moradores={self.n_moradores})")