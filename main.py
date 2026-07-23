import os
from colorama import init, Fore, Style
from app.core.database import Database

# Componentes de Produtos
from app.dao.Produto_dao import Produto_DAO
from app.views.Produto_view import Produto_Terminal_View
from app.controllers.Produto_controller import Produto_Controller

# Componentes de Fornecedores
from app.dao.Fornecedor_dao import Fornecedor_DAO
from app.views.Fornecedores_views import Fornecedores_Terminal_View
from app.controllers.Fornecedor_controller import Fornecedor_controller

# Componentes de Usuários
from app.dao.Usuario_dao import Usuario_DAO
from app.views.Usario_view import Usuario_Terminal_View
from app.controllers.Usuario_controller import Usuario_Controller

# Componentes de CLientes
from app.dao.cliente_dao import cliente_dao
from app.views.Clientes_views import Clientes_Terminal_View
from app.controllers.Cliente_controller import Cliente_Controller

class ErpApplication:
    def __init__(self):
        # Inicializa o colorama interno
        init(autoreset=True)
        
        self._database = Database()  # Inicializa a conexão com o banco de dados

        self._dao_fornecedores = Fornecedor_DAO(self._database)
        self._ctrl_fornecedores = Fornecedor_controller(dao=self._dao_fornecedores, view=Fornecedores_Terminal_View())

        # Inicialização centralizada dos ecossistemas (Container de Serviços manual)
        self._dao_produtos = Produto_DAO(self._database, self._dao_fornecedores)
        self._ctrl_produtos = Produto_Controller(dao=self._dao_produtos, fornecedor_dao=self._dao_fornecedores, view=Produto_Terminal_View())
        
        self._dao_usuarios = Usuario_DAO(self._database)
        self._ctrl_usuarios = Usuario_Controller(dao=self._dao_usuarios, view=Usuario_Terminal_View())        

        self._dao_clientes = cliente_dao(self._database)
        self._ctrl_clientes = Cliente_Controller(dao=self._dao_clientes, view=Clientes_Terminal_View())   

    def _renderizar_menu_principal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + Style.BRIGHT + "=== SISTEMA CORPORATIVO ERP ===")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Fornecedores")
        print("3 - Gerenciar Usuários")
        print("4 - Gerenciar Clientes")
        
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
                self._ctrl_clientes.inicializar_sistema()                               
            else:
                print(Fore.RED + "\nOpção inválida!")
                input(Fore.WHITE + "Pressione Enter para continuar...")



if __name__ == "__main__":
    # Instancia a aplicação que gerencia suas próprias dependências
    app = ErpApplication()
    
    # Inicia o ciclo de vida do sistema
    app.run()