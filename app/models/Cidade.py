from app.models.Estado import Estado
class Cidade:
    def __init__(self, id, nome, estado:Estado):
        self._id = id
        self._nome = nome
        self._Estado = estado


    @property
    def id(self):
       return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def estado(self):
        return self._estado


    