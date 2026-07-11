class Fornecedor_models:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento):
        self.__id = id
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

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @property
    def razao_social(self):
        return self.razao_social
    
    @razao_social.setter
    def razao_social(self, nova_razao_social):
        self.razao_social = nova_razao_social

    @property
    def nome_fantasia(self):
        return self.nome_fantasia
    
    @nome_fantasia.setter
    def nome_fantasia(self, novo_nome_fantasia):
        self.nome_fantasia = novo_nome_fantasia
    
    @property
    def cnpj(self):
        return self.cnpj
    
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj

    @property
    def sla_atendimento(self):
        return self.sla_atendimento
    
    @sla_atendimento.setter
    def sla_atendimento(self, nova_sla_antendimento):
        self.sla_atendimento = nova_sla_antendimento