from config.config import Configurations

class Utils():
    def __init__(self):
        self.__cofing = Configurations()

    def read_file(self):
        with open(self.__cofing.file_output, 'r') as file:
            #map retorna um pornteiro, por isso preciso fazer um casting para uma lista explicitamente
            return list(map(lambda x: x.replace('\n', ''), file.readline()))

    #metodo dentro de classe colocado _no type para entender que não é uma palavra reservada
    def write_file(self, _type, value, description):
        with open(self.__cofing.file_output, 'a+') as file:
            file.write(f'\nOperação: {_type} - Valor: {value} - Descrição: {description}')