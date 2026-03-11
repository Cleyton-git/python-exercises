class Cliente:
    def __init__(self, nome, saldo = 0):
        self.nome = nome
        self.saldo = saldo
        
    def __str__(self):
        return f"O cliente é {self.nome} e seu saldo é {self.saldo}R$"
        
    def salario_caiu(self):
        self.saldo += 1500
        return print(f"O saldo do cliente aumentou em 1500R$ seu novo saldo é {self.saldo}R$")
    
    def cliente_gastou(self, valor):
        self.saldo -= valor
        return print(f"O cliente gastou {valor}R$ seu novo saldo é {self.saldo}R$")
        

cliente1 = Cliente("Cleyton", 1500)
cliente1.salario_caiu()
cliente1.cliente_gastou(1000)
print(cliente1)
