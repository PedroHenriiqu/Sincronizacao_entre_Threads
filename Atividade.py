from threading import Thread

class Atividade(Thread):
    
    def __init__(self, num, conta):
        super().__init__()
        self.operacao = num
        self.conta = conta
        
    def run(self):
        if self.operacao[0].upper() == 'DEPOSITAR':
            self.conta.depositar(self.operacao[1])
            
        elif self.operacao[0].upper() == 'SACAR':
            self.conta.sacar(self.operacao[1])
        else:
            print(f'Erro na operação: {self.operacao}')