class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self, empresa):
        return f"Boa tarde, meu nome é {self.nome} sou um {self.cargo} e trabalho no setor de {self.setor} da empresa {empresa}"
    

func1 = Funcionario("Cleyton", "Solda", "Auxiliar de montagem de peças")
print(func1.apresentacao("Curso em video"))        
