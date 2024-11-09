class Configurations():
    def __init__(self):
        self.__file_output = './out/transactions.txt'
        
    #Quem instaciar a file configuraton pode ver mas não pode editar
    @property
    def file_output(self):
        return self.__file_output