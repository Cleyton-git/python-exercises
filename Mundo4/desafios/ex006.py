class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.estado = False
    
    def destampar(self):
        self.estado = True
    
    def tampar(self):
        self.estado = False
    
    def escrever(self, frase):
        if self.estado == True:
            print(f"{frase} < VC ESCREVEU NA COR {self.cor}")
        else:
            print(f"A caneta esta fechada!")
    
    def quebrar_linha(self, linhas):
        for c in range(0, linhas):
            print("")
            

caneta_azul = Caneta("Azul")
caneta_azul.destampar()
caneta_azul.escrever("Oi tudo bem?")
caneta_azul.quebrar_linha(5)
print("OLHA SO")
        