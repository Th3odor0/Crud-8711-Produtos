class Produto_dao:
    def __init__(self):
        self.__produtos = []
        self.__novo__id = 1

    def save(self, produtos):
        self.__produtos.append(produtos)
        self.__novo__id += 1
        return produtos

    def get_all(self):
        return list(self.__produtos)

    def get_by_id(self, id):
        for p in self.__produtos:
            if p._id == id:
                return p
            return None

    def delete(self, id):
        produto = self.get_by_id(id)
        if produto:
            self.__produtos.remove(produto)
            return True
        return False

    def update(self, produto_atualizado):
        return True