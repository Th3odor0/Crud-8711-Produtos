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
    def calcular_idade(data):
        # 1. Se a data for None ou vazia, retorna 0 sem lançar erro
        if not data:
            return 0

        data_inicio = data

        # 2. Se for string, converte usando a função da própria classe
        if isinstance(data, str):
            try:
                data_inicio = Data_Utils.string_para_data(data)
            except ValueError:
                return 0 # Ou raise ValueError("A data está em um formato inválido.")

        # 3. Se for objeto datetime, converte para date
        elif isinstance(data, datetime):
            data_inicio = data.date()

        # 4. Garante que agora é um objeto date válido
        if not isinstance(data_inicio, date):
            return 0  # Retorna 0 para datas num formato inesperado

        # Cálculo da idade
        hoje = date.today()
        idade = hoje.year - data_inicio.year

        # Ajusta se a pessoa ainda não fez aniversário este ano
        if (hoje.month, hoje.day) < (data_inicio.month, data_inicio.day):
            idade -= 1

        return idade