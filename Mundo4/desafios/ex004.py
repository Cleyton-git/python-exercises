class Livro:
    def __init__(self, nome, paginas):
        self.nome_livro = nome
        self.paginas = paginas
        self.cont = 1
    
    def avancar_pagina(self, numero_paginas):
        for c in range(1, numero_paginas+1):
            if self.cont > self.paginas:
                print("Vc chegou a o final do seu livro!")
                return
            print(f"Pagina = {self.cont}")
            if c == numero_paginas:
                print(f"Vc parou de ler e esta na pagina {self.cont}")
            self.cont += 1
                
                

livro1 = Livro("Sutil arte de ligar o fdc", 20)
livro1.avancar_pagina(10)
livro1.avancar_pagina(9)
livro1.avancar_pagina(1)
