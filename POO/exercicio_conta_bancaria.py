
class ContaBancaria:
    def __init__(self, nome, saldo, ativo = False):
        self.nome = nome
        self.saldo = saldo
        self.ativo = ativo


    def desativar_conta(self):
        print(f'Conta desativada!')
        self.ativo = False
        exit()


    def ativar_conta(self):
        if self.ativo:
            print('Conta ativada!')
            self.ativo = True

             

    def depositar(self, saldo):
        self.saldo = saldo
        self.ativo = True
        if self.ativo:
            saldo = int(input('Escolha o valor do deposito: '))
            print(f'O valor depositado foi: {saldo}')
    

    
    
conta1 = ContaBancaria('Gabriel', '1500', ativo= True)
conta2 = ContaBancaria('Bianca', '10000', ativo= False )
#conta1.desativar_conta()
conta1.ativar_conta()
conta1.depositar(0)



