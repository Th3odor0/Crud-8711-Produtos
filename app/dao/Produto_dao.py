from app.dao.dao import DAO
from app.models.Produto import Produto

class Produto_DAO(DAO):
    def __init__(self, database, fornecedor_dao):
        self.database = database
        self.fornecedor_dao = fornecedor_dao
    def save(self, produto):
        conexao, cursor = self.conectar()
        try:
            sql = """
                INSERT INTO PRODUTO
                (NOME, ESTOQUE, PRECO, FORNECEDOR_ID)
                VALUES (%s, %s, %s, %s)
            """
            fornecedor_id = produto.fornecedor.id if produto.fornecedor else None
            cursor.execute(sql, (
                produto.nome,
                produto.estoque,
                produto.preco,
                fornecedor_id
            ))
            conexao.commit()
            produto.id = cursor.lastrowid
            return produto
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)
    
    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    ID,
                    NOME,
                    ESTOQUE,
                    PRECO,
                    FORNECEDOR_ID
                FROM
                    PRODUTO
                ORDER BY 
                    NOME
            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            produtos = []
            for registro in registros:
                fornecedor_id = registro[4]
                fornecedor = self.fornecedor_dao.get_by_id(fornecedor_id) if fornecedor_id else None
                
                produtos.append(
                    Produto(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        fornecedor
                    )
                )
            return produtos
        except Exception as e:
            raise e
        finally:
            self.desconectar(cursor, conexao)
    
    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    ID,
                    NOME,
                    ESTOQUE,
                    PRECO,
                    FORNECEDOR_ID
                FROM
                    PRODUTO
                WHERE
                    ID = %s
            """        
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            
            # Validação antes de acessar os índices do registro
            if registro is None:
                return None

            fornecedor_id = registro[4]
            fornecedor = self.fornecedor_dao.get_by_id(fornecedor_id) if fornecedor_id else None

            return Produto(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                fornecedor
            )
        except Exception as e:
            raise e
        finally:
            self.desconectar(cursor, conexao)

    def update(self, produto):
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE PRODUTO SET
                    NOME            = %s,
                    ESTOQUE         = %s,
                    PRECO           = %s,
                    FORNECEDOR_ID   = %s
                WHERE
                    ID = %s
            """
            fornecedor_id = produto.fornecedor.id if produto.fornecedor else None
            cursor.execute(sql, (
                produto.nome,
                produto.estoque,
                produto.preco,
                fornecedor_id,
                produto.id
            ))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)
    
    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                DELETE FROM PRODUTO
                WHERE ID = %s
            """
            cursor.execute(sql, (id,))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)