import os
from app.models.Fornecedor_models import Fornecedor_models

class fornecedor_controller:
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
                    rezao_social, nome_fantasia, cnpj = self. view.ler_dados_fornecedores()
                    