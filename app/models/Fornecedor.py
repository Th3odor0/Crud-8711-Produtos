class Fornecedor_models:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento):
        self.id = id
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.sla_atendimento = sla_atendimento

    def tempo_atendimento(self, sla):
        self.sla_atendimento = sla
        if sla < 0:
             raise ValueError("O tempo não pode ser negativo.")
        
    def atualizar_fornecedor(self, nova_razao_social, novo_nome_fantasia, novo_cnpj, novo_sla):
        self.razao_social = nova_razao_social
        self.nome_fantasia = novo_nome_fantasia
        self.cnpj = novo_cnpj
        self.sla_atendimento = novo_sla

