import os
from app.models.Fornecedor import Fornecedor_models

class Fornecedor_controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view

    def inicializar_sistema(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.view.renderizar_menu()
            if opcao == 0:
                self.view.exibir_mensagem("Saindo do sistema...")
                break
            elif opcao == 1:
                try:
                    razao_social, nome_fantasia, cnpj, sla_atendimento= self. view.ler_dados_fornecedores()
                    fornecedor = Fornecedor_models(None, razao_social, nome_fantasia, cnpj, sla_atendimento)
                    self.dao.save(fornecedor)
                    self.view.exibir_mensagem("Fornecedor cadastrado com sucesso!")
                except ValueError:
                    self.view.exibir_mensagem("Erro: Entrada invalida. tente novamente.", False)
                input("Pressione Enter para continuar...")

            elif opcao == 2:
                fornecedor = self.dao.get_all()
                self.view.exibir_fornecedores(fornecedor)
                input("Pressione Enter para continuar...")

            elif opcao == 3:
                try:
                    fornecedor = self.dao.get_all()
                    self.view.exibir_fornecedores(fornecedor)
                    id_fornecedor = int(self.view.ler_id())
                    fornecedor_existente = self.dao.get_by_id(id_fornecedor)
                    if fornecedor_existente:
                        razao_social, nome_fantasia, cnpj, sla_atendimento = self.view.ler_dados_fornecedores()
                        fornecedor_existente.atualizar_fornecedor(razao_social, nome_fantasia, cnpj, sla_atendimento)
                        self.dao.update(fornecedor_existente)
                        self.view.exibir_mensagem("Fornecedor atualizado com sucesso!")
                    else:
                        self.view.exibir_mensagem("Fornecedor não encontrado. ", False) 
                except ValueError as e:
                    self.view.exibir_mensagem(f"Erro: {str(e)}", False)
                input("Pressione Enter para continuar...")
            elif opcao == 4:
                try:
                    fornecedor = self.dao.get_all()
                    self.view.exibir_fornecedores(fornecedor)
                    id_fornecedor = int(self.view.ler_id())
                    sucesso = self.dao.delete(id_fornecedor)
                    if sucesso:
                        self.view.exibir_mensagem("Fornecedor excluido com sucesso!")
                    else:
                        self.view.exibir_mensagem("Fornecedor não encotrado.", False) 
                except ValueError:
                    self.view.exibir_mensagem("Erro: ID invalido", False) 
                input("Pressione Enter para continuar...")
            else:
                self.view.exibir_mensagem("Opção invalida. Tente novamente.", False)
                input("Pressione Enter para continuar...")               