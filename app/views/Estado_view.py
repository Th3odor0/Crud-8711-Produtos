from colorama import init, Fore, Style


init(autoreset=True)

class estado_terminal_view:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE ESTADO (MVC) ==="

    def renderizar_menu(Self):
        print(Fore.CYAN + Style.BRIGHT + Self.titulo_sistema)
        print("1 - Cadastrar Estados")
        print("2 - Listar Estados")
        print("3 - Atulizar Estados")
        print("4 - Excluir Estado")
        print("0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolhe uma opção: "))
        except ValueError:
            return -1
        
    def ler_dados_estado(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE ESTADO ===")
        nome = input("Digite o nome: ")
        sigla = input("Digite a sigla: ")        
        return nome, sigla, 
    
    def ler_id(self):
        return input("Digite o ID do Estado")
    
    def exibir_estado(self, estados):
        print(Fore.YELLOW + "\n--- TABELA DE ESTADOS ---")
        if not estados:
            print("Nenhum Estado Cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<20} | {'SIGLA':<2}")
        print("-"*100)
        for e in estados:
            print(f"{e.id:<4} | {e.nome:<20} | {e.sigla:<20} ")


    def exibir_mensagem(self, mensagem, sucesso=True): 
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")