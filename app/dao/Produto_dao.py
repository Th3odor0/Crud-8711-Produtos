from app.dao.dao import DAO
from app.models.Produto import Produto

class Produto_dao(DAO):
    def __init__(self, database):
        self._database = database    

    def save(self, produto):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
            INSERT INTO PRODUTO
                (NOME, ESTOQUE, PRECO)
                VALUES (%s, %s, %s)
                """
        cursor.execute(sql, (
        produto.nome,
        produto.estoque,
        produto.preco
        ))

        conexao.commit()
        produto.id = cursor.lastrowid
        self._database.desconectar(cursor, conexao)
        return produto
    

    def get_all(self):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                SELECT
                ID,
                NOME,
                ESTOQUE,
                PRECO
            FROM
                PRODUTO
            ORDER BY
                NOME
            """
        cursor.execute(sql)
        registros = cursor.fetchall()
        produto = []
        for registro in registros:
            produto.append(
                Produto(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3]
                )
            )
            
        self._database.desconectar(cursor, conexao)
        return produto

    def get_by_id(self, id):
        return 1
    
    def update(self, objeto):
        return True
    
    def delete(self, id):
        return True