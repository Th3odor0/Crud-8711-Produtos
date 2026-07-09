class Cliente:
    def __init__(self, id, nome, email, data_nascimento, limite_credito):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.limite_credito = limite_credito
        self.email = email

    def validar_limite_credito(self, limite_credito):
        self.limite_credito = limite_credito
        if limite_credito < 0:
            raise ValueError("O limite não pode ser negativo")


    def atualizar_dados(self, novo_nome, novo_email, novo_limite, nova_data_nascimeto):
        self.nome = novo_nome
        self.limite_credito = novo_limite
        self.data_nascimento = nova_data_nascimeto
        self.email = novo_email
              