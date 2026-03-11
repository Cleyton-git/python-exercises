class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []
    
    def add_favoritos(self, jogo_favorito):
        self.jogos_favoritos.append(jogo_favorito)
        
    def ficha_gamer(self):
        print(f"Gamer: {self.nome}")
        print(f"Nickname: {self.nick}")
        self.jogos_favoritos.sort()
        print(f"Jogos Favoritos:", ", ".join(self.jogos_favoritos))


Cleyton = Gamer("Cleyton", "Notycle")
Cleyton.add_favoritos("LoL")
Cleyton.add_favoritos("Little Nightmares 1")
Cleyton.add_favoritos("Little Nightmares 2")
Cleyton.add_favoritos("Sundered")
Cleyton.add_favoritos("Dota")
Cleyton.add_favoritos("Zelda")
Cleyton.ficha_gamer()
        