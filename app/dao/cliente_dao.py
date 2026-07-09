class cliente_dao:
    def __init__(self):
        self.__clientes = []
        self.__novo_id = 1

    def save(self, cliente):
        cliente.id = self.__novo_id
        self.__clientes.append(cliente)
        self.__novo_id += 1
        return cliente
    
    def get_all(self):
        return list(self.__clientes)
    
    def get_by_id(self, id):
        for c in self.__clientes:
            if c.id ==  id:
                return c
            return None
        
    def delete(self, id):
        Clientes = self.get_by_id(id)
        if Clientes:
            self.__clientes.remove(Clientes)
            return True
        return False
    
    def update(self, clientes_atualizado):
        return True