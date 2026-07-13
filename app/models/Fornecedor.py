class Fornecedor_models:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento):
        self.__id = id
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cnpj
        self._sla_atendimento = sla_atendimento

    def tempo_atendimento(self, sla):
        self._sla_atendimento = sla
        if sla < 0:
             raise ValueError("O tempo não pode ser negativo.")
        
    def atualizar_fornecedor(self, nova_razao_social, novo_nome_fantasia, novo_cnpj, novo_sla):
        self._razao_social = nova_razao_social
        self._nome_fantasia = novo_nome_fantasia
        self._cnpj = novo_cnpj
        self._sla_atendimento = novo_sla

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @property
    def razao_social(self):
        return self._razao_social
    
    @razao_social.setter
    def razao_social(self, nova_razao_social):
        self._razao_social = nova_razao_social

    @property
    def nome_fantasia(self):
        return self._nome_fantasia
    
    @nome_fantasia.setter
    def nome_fantasia(self, novo_nome_fantasia):
        self._nome_fantasia = novo_nome_fantasia
    
    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj

    @property
    def sla_atendimento(self):
        return self._sla_atendimento
    
    @sla_atendimento.setter
    def sla_atendimento(self, nova_sla_antendimento):
        self._sla_atendimento = nova_sla_antendimento