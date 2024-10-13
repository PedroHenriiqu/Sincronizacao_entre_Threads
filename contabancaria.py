
import threading

class ContaBancaria:
    
    def __init__(self):
        self.saldo = 0
        self.lock = threading.Lock()
        
    def depositar(self, valor):
        self.lock.acquire()
        self.saldo += int(valor)
        self.lock.release()
        
    def sacar(self, valor):
        self.lock.acquire()
        self.saldo -= int(valor)
        self.lock.release()