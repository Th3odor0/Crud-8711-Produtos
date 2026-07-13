class Usuario:
    def __init__(self, id, nome, email, data_nascimento):
        self.__id = id
        self._nome = nome
        self._email = email
        self._data_nascimento = data_nascimento


    def atualizar_dados(self, novo_nome, novo_email, nova_data_nascimeto):
        self._nome = novo_nome
        self._email = novo_email
        self._data_nascimento = nova_data_nascimeto
        

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
    def email(self):
        return self._email
    
    @email.setter
    def email(self, _novo_email):
        self._email = _novo_email

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, _nova_data_nascimento):
        self._data_nascimento = _nova_data_nascimento