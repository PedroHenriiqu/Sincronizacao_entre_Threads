from Atividade import Atividade
from contabancaria import ContaBancaria

def __leitor_txt():
    dados = []        
    with open('Dados.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.replace("\n", "").replace("-", "").split(",")
            dados.append(linha)
    return dados

def main():
    conta = ContaBancaria()
    dados = __leitor_txt()
    threads = []
    for operacao in dados:
        thr = Atividade(operacao, conta)
        threads.append(thr)
        thr.start()
        
    for thr in threads:
        thr.join()  
        
    print(f'Saldo total da conta: {conta.saldo}')
     

main()