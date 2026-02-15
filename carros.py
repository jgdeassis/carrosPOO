# Classe 
class Veiculo:
    # Atributos da classe pai
    def __init__(self, marca , ano , modelo, speedmax):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.ligado = False
        self.speedmax = speedmax
        self._speed = 0

    # Método que liga o veículo
    # Verifica se o veículo já está ligado
    # Inicie para acelerar o veículo
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O veículo {self.modelo} está ligado.")

        else:
            print(f"O veículo {self.modelo} já estava ligado.")
    # Método que desliga o veículo
    # Verifica se ele está parado antes de desligar
    # Verifica se ele já está desligado
    def desligar(self):
        if self._speed > 0:
            print("Veículo em movimento, impossível desligar")
            return self._speed

        elif self.ligado:
            self.ligado = False
            print(f"O veículo {self.modelo} está desligado.")
            return self._speed

        else:
            print(f"O veículo {self.modelo} já estava desligado.")
            return self._speed
    # Método que imprime os atributos do veículo
    def info(self):
        print(f"Marca:{self.marca} | modelo:{self.modelo} | Ano:{self.ano}" )
    # Método que verifica a velocidade do veículo  
    def get_speed(self):
        return self._speed
    # Método que acelera o veículo
    # Verifica se o veículo está ligado para acelerar
    # Impede acelerar depois da velocidade máxima do veículo
    # Permite acelerar exatamente até o valor da velocidade máxima do veículo
    # Impede acelerar com valores menores ou iguais a 0
    def acelerar(self , valor):
        if not self.ligado:
            print("Impossível acelerar o veículo desligado. ")
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
            return self._speed

    # Método que zera totalmente a velocidade atual do veículo
    # Verifica se o veículo já está com velocidade 0
    def parar(self):
        if self._speed == 0:
            print("Veículo já parado.")
            return
        
        else: 
            print("Parando o veículo.")
            self._speed = 0
    def status(self):
        print(f"Velocidade atual:{self._speed}Km/h | Motor:{self.ligado}")

    # Método que diminui a velocidade atual do veículo
    # Verifica se o veículo está desligado, impedindo o freio no veículo desligado
    # Impede frear com valores menores ou iguais a 0
    # Verifica se o veículo já está parado, impedindo o freio no veículo parado
    # Impede diminuir valores maiores que a velocidade atual, impossibilitando velocidade negativa

    def frear(self , valor):
        if not self.ligado:
            print("Veículo desligado, sem necessidade de frear.")
            return self._speed
            
        if self._speed == 0:
            print("Veículo parado, sem necessidade de frear.")
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
# classe filha(moto)
class Moto(Veiculo):

    # construtor herdado da classe pai 
    def __init__(self, marca, ano, modelo, speedmax, cc):
        super().__init__(marca, ano, modelo, speedmax)
        self.cc = cc
        self.emp = False

    # método herdado da classe pai 
    def status(self):
        super().status()
        if self.emp:
            print(f"| Empinada: {self.emp}")
    # Método que fornece informações específicas da classe filha 
    def info(self):
         print(f"Marca: {self.marca} | Ano:{self.ano} | Modelo: {self.modelo} | Cilindradas: {self.cc}")
    
    # Método herdado da classe pai 
    # Impede a moto desligar estando empinada
    def desligar(self):
        if self.emp:
            print("Moto empinada, impossível desligar.")
            return
        super().desligar()
    # Método que faz a moto empinar
    # Impossibilita a moto a empinar estando com menos de 15Km/h 
    # Impossibilita a moto de empinar estando desligada 
    # Muda o estado para empinar e parar de empinar a moto
    def empinar(self):
        valor = self.get_speed()
        if not self.ligado :
            print("Moto desligada, impossível empinar.")
            return
        
        if valor < 14:
            print("Velocidade atual impossível para empinar. Velocidade mínima: 15Km/h.")
            return self.emp
        
        if self.emp:
            print("Parando de empinar moto.")
            self.emp = False
            return self.emp
        
        if not self.emp:
            print("Empinando moto. CUIDADO!")
            self.emp = True
            return self.emp
    # Método herdado da classe pai 
    # Método que informa quando a moto atinge uma velocidade mínima para empinar 
    def acelerar(self,valor):
       va = super().acelerar(valor)
       if va >= 15 and not self.emp:
           print("Velocidade mínima para empinar a moto atingida!")
           return
    # Método herdado da classe pai 
    # Informa quando a velocidade atual é menor que a necessária para continuar empinando a moto 
    def frear(self , valor):
        vmemp = super().frear(valor)
        if  self.emp == True and self._speed < 15:
                print("Velocidade menor que necessária para continuar empinando a moto.")
                self.emp = False
        return vmemp      
    
    # Método herdado da classe pai 
    # Para de empinar a moto instantâneamente       
    def parar(self):
        if self.emp == True:
            print("Parando de empinar a moto...")
        super().parar()
        
##   EXEMPLO
carro1 = Veiculo("Fiat", 1989 , "uno" , 200)
moto1 = Moto("Yamaha", 2020, "FZ25" , 250 , 300)
moto1.ligar()
moto1.acelerar(15)
moto1.empinar()
moto1.status()

carro1.status() 
carro1.info()
carro1.ligar()
carro1.acelerar(150)
carro1.acelerar(70)
carro1.acelerar(70)
carro1.frear(300)
carro1.desligar()
carro1.parar()
carro1.desligar()
# Forma de listar os veículos e extrair informações sobre eles
veiculos = [ moto1]

for v in veiculos:
    v.info()
     