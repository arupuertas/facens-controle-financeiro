from models.transaction import Transaction

'''
adicionar opção 3
pesquisar por tipo de transação
deletar transação 
'''

class Initialize():
    def show_menu(self):
        print(40 * '-')
        print('Bem-Vindo ao Controle Financeiro')
        print(40 * '-')
        print('1 - Adicionar Transação')
        print('2 - Visualizar Transações')
        print('3 - Deletar Transação')
        print('4 - Sair')

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')
        
        if option not in ['1', '2', '3']:
            print('\nOpção Inválida!')

        return option
        

    def to_add(self):
        operation = input('Informar o tipo da operação: ')
        value = input('Informe o valor: ')
        description = input('Informe a descrição: ')

        t = Transaction(operation, value, description)
        t.save()
        #apagando o objeto depois que uso, não é obrigado a usar
        del t
    
    def to_view(self):
        #instanciando 
        Transaction().view()

    def to_go_out(self):
        print('\nObrigado e Volte Sempre!')

    def to_delete(self):
        Transaction().delete()
        
if __name__ == '__main__':
    init = Initialize()
    option = ''

    while option != '4':
        init.show_menu()
        option = init.choose_option()

        if option == '1':
            init.to_add()
        elif option == '2':
            init.to_view()
        elif option == '3':
            init.to_delete()
        elif option == '4':
            init.to_go_out()
        else:
            print('Opção Não Disponível')
        