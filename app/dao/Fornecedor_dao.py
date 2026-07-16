from app.dao.Generic_dao import Generic_DAO
from app.models.Fornecedor import Fornecedor_models
class Fornecedores_dao(Generic_DAO):
    def __init__(self, database):
        self._database = database    

    def save(self, fornecedor):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
            INSERT INTO FORNECEDOR
                (RAZAO_SOCIAL, NOME_FANTASIA, CNPJ, SLA_ATENDIMENTO)
                VALUES (%s, %s, %s,%s)
                """
        cursor.execute(sql, (
	    fornecedor.razao_social,
        fornecedor.nome_fantasia,
        fornecedor.cnpj,
        fornecedor.sla_atendimento
        ))

        conexao.commit()
        fornecedor.id = cursor.lastrowid
        self._database.desconectar(cursor, conexao)
        return fornecedor
    

    def get_all(self):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                SELECT
                ID,
		RAZAO_SOCIAL,
                NOME_FANTASIA,
                CNPJ,
                SLA_ATENDIMENTO
            FROM
                FORNECEDOR
            ORDER BY
                NOME_FANTASIA
            """
        cursor.execute(sql)
        registros = cursor.fetchall()
        fornecedor = []
        for registro in registros:
            fornecedor.append(
                Fornecedor_models(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4]
                )
            )
            
        self._database.desconectar(cursor, conexao)
        return fornecedor

    def get_by_id(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                SELECT
                ID,
                RAZAO_SOCIAL,
                NOME_FANTASIA,
                CNPJ,
                SLA_ATENDIMENTO
            FROM
                FORNECEDOR
            WHERE
                ID = %s
            """
        cursor.execute(sql,(id,))
        registro = cursor.fetchone()
        self._database.desconectar(cursor, conexao)
        if registro is None:
            return None
        return Fornecedor_models(
            registro[0],
            registro[1],
            registro[2],
            registro[3],
            registro[4]
        )
    
    def update(self, fornecedor):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                UPDATE FORNECEDOR SET
	            RAZAO_SOCIAL     = %s,
                    NOME_FANTASIA    = %s,
                    CNPJ = %s,
                    SLA_ATENDIMENTO   = %s
                WHERE
                    ID = %s
        """
        cursor.execute(sql,(
		    fornecedor.razao_social,
                    fornecedor.nome_fantasia,
                    fornecedor.cnpj,
                    fornecedor.sla_atendimento,
                    fornecedor.id
        ))
        conexao.commit()
        sucesso = cursor.rowcount > 0
        self._database.desconectar(cursor, conexao)
        return sucesso
    
    def delete(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql = """
                DELETE FROM FORNECEDOR
                WHERE ID = %s 
        """
        cursor.commit()
        sucesso = cursor.rowcount > 0
        self._database.desconectar(cursor, conexao)
        return sucesso