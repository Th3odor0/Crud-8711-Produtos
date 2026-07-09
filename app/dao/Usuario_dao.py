class Usuario_dao:
    def __init__(self):
        self.__usuarios = []
        self.__novo__id = 1

    def save(self, usuario):
        usuario.id = self.__novo__id
        self.__usuarios.append(usuario)
        self.__novo__id += 1
        return usuario
    
    def get_all(self):
        return list(self.__usuarios)
    
    def get_by_id(self, id):
        for u in self.__usuarios:
            if u.id == id:
                return u
            return None
        
    def delete(self, id):
        Usuarios = self.get_by_id(id)
        if Usuarios:
            self.__usuarios.remove(Usuarios)
            return True
        return False
    
    def update(self, usuarios_atualizado):
        return True