class Yoshi:
    """
        Essa classe cria um Yoshi que tem cor e lingua
        
        Para criar um use: variavel = Yoshi(cor, lingua)
    """
    def __init__(self, c = "", l = 0):
        self.cor = c
        self.linguaTamanho = l
        
    def linguaFora(self):
        self.linguaTamanho += 1
    
    def __str__(self):
        return f"Seu Yoshi é da cor {self.cor} e tem {self.linguaTamanho}cm's de lingua"
    
    def __getstate__(self):
        return f"A cor é {self.cor} e o tamanho da lingua é {self.linguaTamanho}"
        
y1 = Yoshi("Verde", 20)
y1.linguaFora()
print(y1.__doc__)
print(y1.__dict__)
print(y1.__getstate__())
print(y1.__class__)


