from colorama import init, Fore, Style
from app.core.data_utils import Data_Utils

init(autoreset=True)

class Clientes_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE CLIENTES (MVC) ==="

    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar Clientes")
        print(f"2 - Listar Clientes")
        print(f"3 - Atulizar Cliente")
        print(f"4 - Excluir Cliente")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolhe uma opção: "))
        except ValueError:
            return -1
        
    def ler_dados_Clientes(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE CLIENTES ===")
        nome = input("Digite o nome: ")
        email = input("Digite o seu email: ")        
        data_nascimento = input("Digite a data de nascimento: ")
        limite_credito = float(input("Digite o limite: "))
        return nome, email, data_nascimento, limite_credito
    
    def ler_id(self):
        return input("Digite o ID do Cliente")
    
    def exibir_clientes(self, clientes):
        print(Fore.YELLOW + "\n--- TABELA DE CLIENTES ---")
        if not clientes:
            print("Nenhum Cliente Cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<20} | {'email':<18}  | {'DATA DE NASCIMENTO'} |{'Idade':<2} | {'limite':<10}")
        print("-"*100)
        for c in clientes:
            print(f"{c.id:<4} | {c.nome:<20} | {c.email:<20} | {Data_Utils.data_para_string(c.data_nascimento):<10} | {c.idade:<2} | {c.limite_credito:<10}")


    def exibir_mensagem(self, mensagem, sucesso=True): 
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")