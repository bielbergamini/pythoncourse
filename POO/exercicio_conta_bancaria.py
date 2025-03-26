
class ContaBancaria:
    def __init__(self, nome, saldo_conta=0, ativo = False):
        self.nome = nome
        self.saldo = saldo_conta
        self.ativo = ativo


    def desativar_conta(self):
        print(f'Conta de {self.nome} desativada!')
        self.ativo = False
        exit()


    def ativar_conta(self):
        if not self.ativo:
            print(f'Conta de {self.nome} ativada!')
            self.ativo = True
        else:
            print(f'Conta de {self.nome} ja está ativa!')

             

    def depositar(self):
        if not self.ativo:
            print("Não é possível depositar. A conta está desativada!")
            return
            
        
    
        valor = float(input('Escolha o valor do depósito: '))
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
            print(f'Saldo atual: R${self.saldo:.2f}')
        else:
            print('O valor do depósito deve ser maior qu zero.')


    def sacar(self):
        if not self.ativo:
            print('Não é possivel sacar, a conta está desativada!')
            return
        
        valor = float(input('Digite o valor a sacar: '))
        if valor <= 0:
            print('O valor deve ser maior que zero')
        elif valor > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Você sacou R${valor:.2f}')
            print(f'Saldo atual: R${self.saldo:.2f}')

    
    def exibir_saldo(self):
        print(f'Saldo de {self.nome}: R${self.saldo:.2f}')

       

           

    
    
conta1 = ContaBancaria('Gabriel', 1500, ativo= True)
conta2 = ContaBancaria('Bianca', 10000, ativo= False )


conta1.exibir_saldo()
conta1.depositar()
conta1.sacar()



