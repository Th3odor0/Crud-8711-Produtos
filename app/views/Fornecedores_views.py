from colorama import init, Fore, Style

init(autoreset=True)

class Fornecedores_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE FORNECEDORES (MVC) ==="

    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print("1 - Cadastrar Fornecedores")
        print("2 - Listar Fornecedores")
        print("3 - Atulizar Fornecedores")
        print("4 - Excluir Fornecedores")
        print("0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolhe uma opção: "))
        except ValueError:
            return -1
        
    def ler_dados_fornecedores(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE FORNECEDORES ===")
        razao_social = input("Digite a razão social da empresa: ")
        nome_fantasia = input("Digite o nome fantasia da empresa: ")        
        cnpj = input("Digite o CNPJ da empresa: ")
        sla_atendimento = input("Digite o SLA do fornecedor: ")
        return razao_social, nome_fantasia, cnpj, sla_atendimento
    
    def ler_id(self):
        return input("Digite o ID do Fornecedor")
    
    def exibir_fornecedores(self, fornecedores):
        print(Fore.YELLOW + "\n--- TABELA DE FORNECEDORES ---")
        if not fornecedores:
            print("Nenhum Fornecedor Cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<20} | {'CNPJ':<18}")
        print("-"*62)
        for f in fornecedores:
            print(f"{f.id:<4} | {f.razao_social:<20} | {f.cnpj:<18}")


    def exibir_mensagem(self, mensagem, seucesso=True):
        cor = Fore. GREEN if seucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")