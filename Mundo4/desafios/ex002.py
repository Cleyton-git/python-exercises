class Produto:
    def __init__(self, produto, preço):
        self.produto = produto
        self.preço = preço
    
    def show_etiqueta(self):
        return f"Produto: {self.produto} \nPreço = {self.preço}R$"
    
danone = Produto("Danone", 10)
print(danone.show_etiqueta())

