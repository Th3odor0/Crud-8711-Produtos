import os
from app.models.Usuario import Usuario


class Usuario_controller:
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
                    nome, email, data_nascimento = self.view.ler_dados_usuarios()
                    usuario = Usuario(None, nome, email, data_nascimento)
                    self.dao.save(usuario)
                    self.view.exibir_mensagem("Usuario cadastrado com sucesso!")
                except ValueError:
                    self.view.exibir_mensagem("Erro: Entrada invalida. tente novamente.", False)
                input("Pressione Enter para continuar...")

            elif opcao == 2:
                usuario = self.dao.get_all()
                self.view.exibir_usuario(usuario)
                input("Pressione Enter para continuar...")

            elif opcao == 3:
                try:
                    usuario = self.dao.get_all()
                    self.view.exibir_usuario(usuario)
                    id_usuario = int(self.view.ler_id())
                    usuario_existente = self.dao.get_by_id(id_usuario)
                    if usuario_existente:
                        nome, email, data_nascimento = self.view.ler_dados_usuarios()
                        usuario_existente.atualizar_dados(nome, email, data_nascimento)
                        self.dao.update(usuario_existente)
                        self.view.exibir_mensagem("Usuario atualizado com sucesso!")
                    else:
                        self.view.exibir_mensagem("Usuario não encontrado. ", False)
                except ValueError as e:
                    self.view.exibir_mensagem(f"Erro: {str(e)}", False)
                input("Pressione Enter para continuar...")
            elif opcao == 4:
                try:
                    usuario = self.dao.get_all()
                    self.view.exibir_usuario(usuario)
                    id_usuario = int(self.view.ler_id())
                    sucesso = self.dao.delete(id_usuario)
                    if sucesso:
                        self.view.exibir_mensagem("Usuario exluido com sucesso!")
                    else:
                        self.view.exibir_mensagem("Usuario não encontrado.", False)
                except ValueError:
                    self.view.exibir_mensagem("Erro: ID invalido", False)
                input("Pressione Enter para continuar...")
            else:
                self.view.exibir_mensagem("Opção invalida, Tente novamente.", False)
                input("Pressione Enter para continuar...")