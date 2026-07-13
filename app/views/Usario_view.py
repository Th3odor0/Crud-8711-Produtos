from colorama import init, Fore, Style

init(autoreset=True)

class Usuarios_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE USUARIOS (MVC) ==="

    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar Usuario")
        print(f"2 - Listar Usuario")
        print(f"3 - Atulizar Usuario")
        print(f"4 - Excluir Usuarios")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolhe uma opção: "))
        except ValueError:
            return -1
        
    def ler_dados_usuarios(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE USUARIOS ===")
        nome = input("Digite o nome: ")
        email = input("Digite o seu email: ")        
        data_nascimento = input("Digite a data de nascimento: ")
        return nome, email, data_nascimento
    
    def ler_id(self):
        return input("Digite o ID do Usuario")
    
    def exibir_usuario(self, usuarios):
        print(Fore.YELLOW + "\n--- TABELA DE USUARIOS ---")
        if not usuarios:
            print("Nenhum Usuario Cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<31} | {'CNPJ':<18} | {'DATA DE NASCIMENTO':<18}")
        print("-"*62)
        for f in usuarios:
            print(f"{f.id:<4} | {f.nome:<20} | {f.email:<20} | {f.data_nascimento:<18}")


    def exibir_mensagem(self, mensagem, seucesso=True):
        cor = Fore. GREEN if seucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")