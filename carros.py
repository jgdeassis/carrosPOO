# Classe 
class Carro:
    # Atributos da classe
    def __init__(self, marca , ano , modelo, speedmax):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.ligado = False
        self.speedmax = speedmax
        self._speed = 0

    # Método que liga o carro
    # Verifica se o carro já está ligado
    # Inicie para acelerar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} está ligado.")

        else:
            print(f"O {self.modelo} já estava ligado.")
    # Método que desliga o carro
    # Verifica se ele está parado antes de desligar
    # Verifica se ele já está desligado
    def desligar(self):
        if self._speed > 0:
            print("Carro em movimento, impossível desligar")

        elif self.ligado:
            self.ligado = False
            print(f"O {self.modelo} está desligado.")

        else:
            print(f"O {self.modelo} já estava desligado.")
    # Método que imprime os atributos do carro
    def info(self):
        print(f"Marca:{self.marca} ,modelo:{self.modelo} ,ano:{self.ano}." )
    # Método que verifica a velocidade do carro  
    def get_speed(self):
        return self._speed
    # Método que acelera o carro
    # Verifica se o carro está ligado para acelerar
    # Impede acelerar depois da velocidade máxima do carro
    # Permite acelerar exatamente até o valor da velocidade máxima do carro
    # Impede acelerar com valores menores ou iguais a 0
    def acelerar(self , valor):
        if not self.ligado:
            print("Impossível acelerar o carro desligado. ")
            return self._speed
        
        if self._speed == self.speedmax:
            print(f"Velocidade máxima já atingida {self.speedmax}Km/h ")
            return self._speed
        
        if valor + self._speed > self.speedmax:
            valor = self.speedmax - self._speed
            print(f"Só é possível aumentar {valor}Km/h")
            print(f"Velocidade máxima atingida {self.speedmax}Km/h")
            self._speed = self.speedmax
            return self._speed
        
        if valor > 0:
            self._speed += valor
            print(f"Velocidade aumentada em {valor}.\n Atual {self._speed}Km/h")
            return self._speed
        
        else: 
            print("Impossível aumentar valores iguais ou menores que 0.")

    # Método que zera totalmente a velocidade atual do carro
    # Verifica se o carro já está com velocidade 0
    def parar(self):
        if self._speed == 0:
            print("Carro já parado.")
            return
        
        else: 
            print("Parando o carro.")
            self._speed = 0

    # Método que diminui a velocidade atual do carro
    # Verifica se o carro está desligado, impedindo o freio no carro desligado
    # Impede frear com valores menores ou iguais a 0
    # Verifica se o carro já está parado, impedindo o freio no carro parado
    # Impede diminuir valores maiores que a velocidade atual, impossibilitando velocidade negativa
    def frear(self , valor):
        if not self.ligado:
            print("Carro desligado, sem necessidade de frear.")
            return self._speed
            
        if self._speed == 0:
            print("Carro parado, sem necessidade de frear.")
            return self._speed
        
        if valor <= 0:
            print("Impossível diminuir valores menores ou iguais a 0.")
            return self._speed
        
        if valor > self._speed:
            print("Impossível diminuir valores maiores que a velocidade atual.")
            return self._speed
        
        else:
            self._speed -= valor
            print(f"Velocidade diminuida em {valor}. \nAtual {self._speed}Km/h")
            return self._speed
        
##   EXEMPLO
carro1 = Carro("Fiat", 1989 , "uno" , 200)
carro1.ligar()
carro1.acelerar(150)
carro1.acelerar(70)
carro1.acelerar(70)
carro1.frear(300)
carro1.desligar()
carro1.parar()
carro1.desligar()
