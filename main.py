import os
from colorama import init, Fore, Style
from app.core.database import Database


# Componentes de Fornecedores
from app.dao.Produto_dao import Produto_dao
from app.views.Produto_view import Produto_Terminal_View
from app.controllers.Produto_controller import Produto_Controller

from app.dao.Fornecedor_dao import Fornecedores_dao
from app.views.Fornecedores_views import Fornecedores_Terminal_View
from app.controllers.Fornecedor_controller import Fornecedor_controller

from app.dao.Usuario_dao import Usuario_dao
from app.views.Usario_view import Usuarios_Terminal_View
from app.controllers.Usuario_controller import Usuario_controller

from app.dao.cliente_dao import cliente_dao
from app.views.Clientes_views import Clientes_Terminal_View
from app.controllers.Cliente_controller import Cliente_controller

class ErpApplication:
    def __init__(self):
        # Inicializa o colorama interno
        init(autoreset=True)
        
        self.database = Database()

        # Inicialização centralizada dos ecossistemas (Container de Serviços manual)
        self._dao_produtos = Produto_dao(self.database)
        self._ctrl_produtos = Produto_Controller(dao=self._dao_produtos, view=Produto_Terminal_View())
        
        self._dao_fornecedores = Fornecedores_dao(self.database)
        self._ctrl_fornecedores = Fornecedor_controller(dao=self._dao_fornecedores, view=Fornecedores_Terminal_View())

        self._dao_usuarios = Usuario_dao(self.database)
        self._ctrl_usuarios = Usuario_controller(dao=self._dao_usuarios, view=Usuarios_Terminal_View())

        self._dao_cliente = cliente_dao(self.database)
        self._ctrl_cliente = Cliente_controller(dao=self._dao_cliente, view=Clientes_Terminal_View())


    def _renderizar_menu_principal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + Style.BRIGHT + "=== SISTEMA CORPORATIVO ERP ===")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Fornecedores")
        print("3 - Gerenciar Usuários")
        print("4-  Gerenciar Clientes")
        print("0 - Sair do Sistema")
        print(Fore.GREEN + "==================================")
        try:
            return int(input("Escolha o módulo: "))
        except ValueError:
            return -1

    def run(self):
        while True:
            opcao = self._renderizar_menu_principal()
            
            if opcao == 0:
                print("\nEncerrando sistema corporativo...")
                break
            elif opcao == 1:
                self._ctrl_produtos.inicializar_sistema()
            elif opcao == 2:
                self._ctrl_fornecedores.inicializar_sistema()
            elif opcao == 3:
                self._ctrl_usuarios.inicializar_sistema()
            elif opcao == 4:
                self._ctrl_cliente.inicializar_sistema()
            else:
                print(Fore.RED + "\nOpção inválida!")
                input(Fore.WHITE + "Pressione Enter para continuar...")


if __name__ == "__main__":
    app = ErpApplication()
    app.run()