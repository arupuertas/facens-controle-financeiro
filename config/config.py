class Configurations():
    def __init__(self):
        self.__file_output = './out/transactions.txt'
        
    #Quem instanciar a file configuration pode ver mas não pode editar
    @property
    def file_output(self):
        return self.__file_output