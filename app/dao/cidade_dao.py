from app.dao.dao import DAO
from app.models.Cidade import Cidade

class cidade_dao(DAO):
    def __init__(self, database):
        self._database = database

    def save(self, cidade):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql ="""
                INSERT INTO CIDADE
                (ID, NOME, ESTADO)
                VALUES (%s, %s, %s)
"""

        cursor.execute(sql,(
            cidade.id,
            cidade.nome,
            cidade.estado
        ))
        conexao.commit()
        cidade.id = cursor.lastrowoid
        self._database.desconectar(cursor, conexao)
        return cidade
    

    def get_all(self):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                SELECT
                    ID,
                    NOME,
                    ESTADO
                FROM
                    CIDADE
                ORDER BY
                    NOME
""" 
        cursor.execute(sql)
        registros = cursor.fetchall()
        cidade = []
        for registro in registros:
            cidade.append(
                Cidade(
                    registro[0],
                    registro[1],
                    registro[2]
                )
            )
        self._database.desconectar(cursor, conexao)
        return cidade
    
    def get_by_id(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                SELECT
                    ID,
                    NOME,
                    ESTADO
                FROM
                    CIDADE
                WHERE
                    ID = %s
"""

        cursor.execute(sql,(id))
        registro = cursor.fetchone()
        self._database.desconectar(cursor, conexao)
        if registro is None:
            return None
        return Cidade(
            registro[0],
            registro[1],
            registro[2]
        )
    
    def update(self, cidade):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                UPDATE CIDADE SET
                NOME = %s,
                ESTADO = %s
            WHERE
                ID = %s
"""

        cursor.execute(sql,(
            cidade.nome,
            cidade.estado
        ))
        conexao.commit()
        sucesso = cursor.rowcount > 0
        self._database.desconectar(cursor, conexao)
        return sucesso
    
    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                DELETE FROM CIDADE
                WHERE ID = %s
            """
            cursor.execute(sql, (id))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception as e:
            conexao.rolback()
            raise e
        finally:
            self.desconectar(cursor, conexao)