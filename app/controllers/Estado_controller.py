import os
from app.models.Estado import Estado


class estado_controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view

    def inicializar_sistema(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.view.renderizar_menu()
            if opcao == 0:
                break
            elif opcao == 1:
                try:
                    nome, sigla = self.view.ler_dados_estado()
                    estado = Estado(None,nome,sigla)
                    self.dao.save(estado)
                    self.view.exibir_mensagem("Estado cadastrado com sucesso!")
                except ValueError:
                    self.view.exibir_mensagem("Erro: Entrada invalida. Tente novamente.", False)
                except KeyboardInterrupt:
                    self.view.exibir_mensagem("Operação cancelada pelo usuario.", False)


            elif opcao == 2:
                estados = self.dao.get_all()
                self.view.exibir_estado(estados)
                self.view.aguardar_entrada()

            elif opcao == 3:
                try:
                    estados = self.dao.get_all()
                    self.view.exibir_estados(estados)
                    id_estado = int(self.view.ler_id())
                    estado_exixtente = self.dao.get_by_id(id_estado)
                    if estado_exixtente:
                        nome, sigla = self.view.ler_dados_estado()
                        estado_exixtente.atualizar_dados(nome, sigla)
                        self.dao.update(estado_exixtente)
                        self.view.exibir_mensagem("Estado atualizado com sucesso!")
                    else:
                        self.view.exibir_mensagem("Estado não encontrado.", False)
                except ValueError as e:
                    self.view.exibir_mensagem(f"Erro: {str(e)}", False)


            elif opcao == 4:
                try:
                    estados = self.dao.get_all()
                    self.view.exibir_estados(estados)
                    id_estado = int(self.view.ler_id())
                    sucesso = self.dao.delete(id_estado)
                    if sucesso:
                        self.view.exibir_mensagem("Estado excluido com sucesso!")
                    else:
                        self.view.exibir_mensagem("Estado não encotrado.", False)
                except ValueError:
                    self.view.exibibr_mensagem("Erro: ID invalido", False)

            else:
                self.view.exibir_mensagem("Opção inavlida. Tente novamente.", False)