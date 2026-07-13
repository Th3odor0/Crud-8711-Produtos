import os
from app.models.Cliente import Cliente

class Cliente_controller:
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
                    nome, email, data_nascimento, limite_credito = self.view.ler_dados_Clientes()
                    cliente = Cliente(None, nome, email, data_nascimento, limite_credito)
                    self.dao.save(cliente)
                    self.view.exibir_mensagem("Cliente cadastrado com sucesso!")
                except ValueError:
                    self.view.exibir_mensagem("Erro: Entrada invalida. tente novamente.", False)
                input("Pressione Enter para continuar...")

            elif opcao == 2:
                cliente = self.dao.get_all()
                self.view.exibir_clientes(cliente)
                input("Pressione Enter para continuar...")

            elif opcao == 3:
                try:
                    cliente = self.dao.get_all()
                    self.view.exibir_clientes(cliente)
                    id_cliente = int(self.view.ler_id())
                    cliente_existente = self.dao.get_by_id(id_cliente)
                    if cliente_existente:
                        nome, email, data_nascimento, limite_credito = self.view.ler_dados_Clientes()
                        cliente_existente.atualizar_dados(nome, email, limite_credito, data_nascimento)
                        self.dao.update(cliente_existente)
                        self.view.exibir_mensagem("Cliente atualizado com sucesso!")
                    else:
                        self.view.exibir_mensagem("Cliente não encontrado. ", False) 
                except ValueError as e:
                    self.view.exibir_mensagem(f"Erro: {str(e)}", False)
                input("Pressione Enter para continuar...")
            elif opcao == 4:
                try:
                    cliente = self.dao.get_all()
                    self.view.exibir_clientes(cliente)
                    id_cliente = int(self.view.ler_id())
                    sucesso = self.dao.delete(id_cliente)
                    if sucesso:
                        self.view.exibir_mensagem("Cliente excluido com sucesso!")
                    else:
                        self.view.exibir_mensagem("Cliente não encotrado.", False) 
                except ValueError:
                    self.view.exibir_mensagem("Erro: ID invalido", False) 
                input("Pressione Enter para continuar...")
            else:
                self.view.exibir_mensagem("Opção invalida. Tente novamente.", False)
                input("Pressione Enter para continuar...")               