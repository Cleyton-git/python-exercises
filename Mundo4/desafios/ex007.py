class ControleRemoto:
    def __init__(self, canal, volume =100):
        self.canal = canal
        self.volume = volume
        self.status = False
    
    def ligar_TV(self):
        self.status = True
        print("TV LIGADA")
        return True
    
    def canais_volume(self):
        print("------------------------------------------------")
        print("0 1 2 3 4 5 - CANAIS")
        print("2 4 6 8 10 - VOLUME")
        print("+ e - - para aumentar/abaixar o volume")
        print("> e < - para mudar de canal")
        print("@ para desligar a TV")
        print(f"Volume: {self.volume}")
        print(f"Canal: {self.canal}")
        print("------------------------------------------------")
    
    def volume_controle(self, flag):
        if flag:
            if self.volume >= 10:
                print("------------------------------------------------")
                print("A TV ja esta em volume maximo!")
                print("------------------------------------------------")
                return
            else:
                self.volume += 2
        if flag == False:
            self.volume -= 2
            if self.volume <= 0:
                print("------------------------------------------------")
                print("A TV agora esta mutada!")
                print("------------------------------------------------")
                self.volume = 0
                
    def mudar_canal(self, op):
        if op == ">":
            if self.canal == 5:
                print("Você ja esta no ultimo canal")
            else:
                self.canal += 1
        else:
            if self.canal == 0:
                print("Você ja esta no primeiro canal")
            else:
                self.canal -= 1
    
c1 = ControleRemoto(1, 0)

while True:
    op = input("LIGAR TV? [S/N]: ").upper()
    if op == "S":
        flag = c1.ligar_TV()
        while flag == True:
            c1.canais_volume()
            op2 = input("Faça uma escolha: ")
            if op2 == "+":
                c1.volume_controle(True)
            elif op2 == "-":
                c1.volume_controle(False)
            elif op2 == "@":
                print("TV desligada!")
                flag = False
            elif op2 == ">":
                c1.mudar_canal(op2)
            elif op2 == "<":
                c1.mudar_canal(op2)
            else:
                print("Opção invalida! Redigite por favor")
                
    elif op == "N":
        print("Vc esta soltando o controle")
        break
    else:
        print("Solicitação invalida, redigite! ")
        