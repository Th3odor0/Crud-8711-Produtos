from datetime import datetime, date

class Data_Utils:

#d= dia de 2 digitos, m= mes de 2 digitos, y= ano de 4 digitos

    FOMATO_DATA =  "%d/%m/%Y"

#recebo um objeto texto(string) e converto para data e volta para o objeto data
    @staticmethod
    def string_para_data(data):
        return datetime.strptime(data,Data_Utils.FOMATO_DATA).date()

#recebo uma data e converto para texto(string)
    @staticmethod
    def data_para_string(data):
        return data.strFtime(Data_Utils.FOMATO_DATA)
#tentativa de converter texto para data, se der certo True, caso ocontrario retorna False    
    @staticmethod
    def validar_data(data):
        try:
            datetime.strptime(data, Data_Utils.FOMATO_DATA)
            return True
        except ValueError:
            return False

    @staticmethod
    def calcular_idade(data):
        data_inicio = Data_Utils.string_para_data(data)
        #data_inicio é objeto de data com a data informada
        hoje = data.today()
        #objeto data com a data de hj
        idade = hoje.year - data_inicio.year
        if(hoje.month, hoje.day,) < (data_inicio.month, data_inicio.day):
            idade -= 1
            return idade