from app.core.data_utils import Data_Utils

class Cliente:
    def __init__(self, id, nome, email, data_nascimento, limite_credito):
        self.__id = id
        self._nome = nome
        self._email = email                     # Corrigido: email com email
        self._data_nascimento = data_nascimento # Corrigido: data com data
        self._limite_credito = limite_credito   # Corrigido: limite com limite

    def validar_limite_credito(self, limite_credito):
        if limite_credito < 0:
            raise ValueError("O limite não pode ser negativo")
        self._limite_credito = limite_credito

    def atualizar_dados(self, novo_nome, novo_email, novo_limite, nova_data_nascimento):
        self._nome = novo_nome
        self._email = novo_email
        self._data_nascimento = nova_data_nascimento # Corrigido: data com nova_data
        self._limite_credito = novo_limite           # Corrigido: limite com novo_limite
              

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        self._data_nascimento = nova_data_nascimento
    

    @property
    def limite_credito(self):
        return self._limite_credito
    
    @limite_credito.setter
    def limite_credito(self, novo_limite_credito):
        self._limite_credito = novo_limite_credito

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def idade(self):
        return Data_Utils.calcular_idade(self._data_nascimento)
    

    