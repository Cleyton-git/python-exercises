#Declaração de classe
class Yoshi:
    def __init__(self): # Método construtor
        #Atributos de instancia
        self.cor = ""
        self.linguaTamanho = 0
    
    #Métodos de instancia
    def linguaFora(self):
        self.linguaTamanho += 1
        return f"A lingua do Yoshi agora tem {self.linguaTamanho}cm"
    
    def mensagem(self):
        return f"Seu Yoshi é da cor {self.cor} e tem {self.linguaTamanho}cm's de lingua"

#Declaração de objetos
y1 = Yoshi()
y1.cor = "Verde"
y1.linguaTamanho = 20
y1.linguaFora()
print(y1.mensagem())

y2 = Yoshi()
y2.cor = "Vermelha"
y2.linguaTamanho = 30
y2.linguaFora()
print(y2.mensagem())