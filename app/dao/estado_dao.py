from app.dao.dao import DAO
from app.models.Estado import Estado

class estado_dao(DAO):
    def __init__(self, database):
        self._database = database

    def save(self, estado):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql ="""
                INSERT INTO ESTADO
                (ID, NOME, SIGLA)
                VALUES (%s, %s, %s)
"""

        cursor.execute(sql,(
            estado.id,
            estado.nome,
            estado.sigla
        ))
        conexao.commit()
        estado.id = cursor.lastrowoid
        self._database.desconectar(cursor, conexao)
        return estado

    def get_all(self):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                SELECT
                    ID,
                    NOME,
                    SIGLA
                FROM 
                    ESTADO
                ORDER BY
                    NOME
"""
        cursor.execute(sql)
        registros = cursor.fetchall()
        estado = []
        for regitro in registros:
            estado.append(
                Estado(
                    regitro[0],
                    regitro[1],
                    regitro[2],
                    regitro[3]
                )
            )
        self._database.desconectar(cursor, conexao)
        return estado

    def get_by_id(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                SELECT
                    ID,
                    NOME,
                    SIGLA
                FROM 
                    ESTADO
                WHERE
                    ID = %s
"""
        cursor.execute(sql,(id,))
        registro = cursor.fetchone()
        self._database.desconectar(cursor, conexao)
        if registro is None:
            return None
        return Estado(
            registro[0],
            registro[1],
            registro[2],
            registro[3]
        )


    def update(self, estado):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                    UPDATE ESTADO SET
                    NOME = %s,
                    SIGLA = %s
                WHERE
                    ID = %s
"""
        cursor.execute(sql,(
        estado.nome,
        estado.sigla
        ))
        conexao.commit()
        sucesso = cursor.rowcount > 0
        self._database.desconectar(cursor, conexao)
        return sucesso

    def delete(self, id):
        return super().delete(id)
        