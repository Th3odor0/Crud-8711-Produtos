from datetime import datetime, date

class Data_Utils:

    # d= dia de 2 digitos, m= mes de 2 digitos, Y= ano de 4 digitos
    FOMATO_DATA = "%d/%m/%Y"

    # recebo um objeto texto(string) e converto para data e volta para o objeto data
    @staticmethod
    def string_para_data(data_texto):
        return datetime.strptime(data_texto, Data_Utils.FOMATO_DATA).date()

    # recebo uma data e converto para texto(string)
    @staticmethod
    def data_para_string(data_objeto):
        # Correção: strftime com 'f' minúsculo
        return data_objeto.strftime(Data_Utils.FOMATO_DATA)

    # tentativa de converter texto para data, se der certo True, caso contrário retorna False    
    @staticmethod
    def validar_data(data_texto):
        try:
            datetime.strptime(data_texto, Data_Utils.FOMATO_DATA)
            return True
        except ValueError:
            return False

    @staticmethod
    def calcular_idade(data_texto):
        # Convertemos o texto recebido para um objeto date
        data_inicio = Data_Utils.string_para_data(data_texto)
        
        # Correção: Mudado de 'data.today()' para 'date.today()' da biblioteca nativa
        hoje = date.today()
        
        # Faz o cálculo inicial da idade baseado no ano
        idade = hoje.year - data_inicio.year
        
        # Verifica se a pessoa ainda não fez aniversário no ano corrente
        if (hoje.month, hoje.day) < (data_inicio.month, data_inicio.day):
            idade -= 1
            
        # Correção: O return foi movido para fora do IF para sempre retornar a idade calculada
        return idade