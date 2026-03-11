class Churrasco:
    def __init__(self, nome_churras, quantidade_p):
        self.nome_churras = nome_churras
        self.quantidade_p = quantidade_p
    
    def analisar(self):
        carne_quantidade_kg = 400 * self.quantidade_p / 1000
        custo = carne_quantidade_kg * 82.40 / self.quantidade_p
        print(f"Analisando o {self.nome_churras} com {self.quantidade_p} convidados")
        print(f"Cada participante comerá 0,4g e cada kilo custo R$82")
        print(f"O custo total será de {carne_quantidade_kg * 82.40:.2f}R$")
        print(f"Cada um terá que pagar R${custo:.2f}")
        return
        
        
churras1 = Churrasco("Churras1", 100)
churras1.analisar()
    