class Fornecedores_dao():
    def __init__(self):
        self.__fornecedores = []
        self.__novo_id = 1

    def save(self, fornecedores):
        self.__nome_fantasia.append(fornecedores)
        self.__id += 1
        return fornecedores
    
    def get_all(self):
        return list(self.__fornecedores)
    
    def get_by_id(self, id):
        for f in self.__fornecedores:
            if f._id == id:
                return f
            return None
        
    def delete(self, id):
        Fornecedores = self.get_by_id(id)
        if Fornecedores:
            self.__fornecedores.remove(Fornecedores)
            return True
        return False
    def update(self, fornecedores_atualizado):
        return True    