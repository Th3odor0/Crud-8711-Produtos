from app.core.data_utils import Data_Utils

class Cliente:
    def __init__(self, id, nome, email, data_nascimento, limite_credito):
        self.__id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.limite_credito = limite_credito
        self.email = email

    def validar_limite_credito(self, limite_credito):
        self.limite_credito = limite_credito
        if limite_credito < 0:
            raise ValueError("O limite não pode ser negativo")


    def atualizar_dados(self, novo_nome, novo_email, novo_limite, nova_data_nascimeto):
        self.nome = novo_nome
        self.limite_credito = novo_limite
        self.data_nascimento = nova_data_nascimeto
        self.email = novo_email
              

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome

    @property
    def data_nascimento(self):
        return self.data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        self.data_nascimento = nova_data_nascimento
    

    @property
    def limite_credito(self):
        return self.limite_credito
    
    @limite_credito.setter
    def limite_credito(self, novo_limite_credito):
        self.limite_credito = novo_limite_credito

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, novo_email):
        self.email = novo_email

    @property
    def idade(self):
        return Data_Utils.calcular_idade(self.data_nascimento)