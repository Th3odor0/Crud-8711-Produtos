from datetime import datetime, date

class Data_Utils:

    # d = dia de 2 dígitos, m = mês de 2 dígitos, Y = ano de 4 dígitos
    FOMATO_DATA = "%d/%m/%Y"

    # Recebe um objeto texto (string) e converto para objeto date
    @staticmethod
    def string_para_data(data_texto):
        if not data_texto:
            return None
        return datetime.strptime(data_texto, Data_Utils.FOMATO_DATA).date()

    # Recebe uma data e converto para texto (string)
    @staticmethod
    def data_para_string(data_objeto):
        # Se for None, retorna uma string vazia
        if data_objeto is None:
            return ""
        return data_objeto.strftime(Data_Utils.FOMATO_DATA)

    # Tentativa de converter texto para data, se der certo True, caso contrário False
    @staticmethod
    def validar_data(data_texto):
        if not data_texto:
            return False
        try:
            datetime.strptime(data_texto, Data_Utils.FOMATO_DATA)
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def calcular_idade(data_texto):
        # Convertemos o texto recebido para um objeto date
        data_inicio = Data_Utils.string_para_data(data_texto)
        
        # Correção: Mudado de 'data.today()' para 'date.today()' da biblioteca nativa
        hoje = date.today()
        idade = hoje.year - data_inicio.year

        # Ajusta se a pessoa ainda não fez aniversário este ano
        if (hoje.month, hoje.day) < (data_inicio.month, data_inicio.day):
            idade -= 1

        return idade