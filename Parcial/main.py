class Personaje():

    def __init__(self, vida=100, posicion=0, velocidad=0):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad

    def recibir_ataque(self, cantidad):
        if (cantidad < self.vida):
            self.vida -= cantidad
            print('recibio un ataque, su vida quedo en ' + str(self.vida))
        else:
            self.vida = 0
            print('el personaje se quedo sin vida')

    def mover(self, destino, velocidad):
        if (velocidad <= 0): return
        print('moviendose desde ' + str(self.posicion) + ' hasta ' + str(destino) + ' con una velocidad de ' + str(velocidad))
        # implementar-----------------------------------------------------------------
        loops = int(abs((self.posicion-destino))/velocidad)
        if (self.posicion > destino):
            for x in range(loops):
                print(self.posicion)
                self.posicion -= velocidad
            print(self.posicion)
            if (self.posicion != destino):
                self.posicion = destino
                print(self.posicion)

        elif(self.posicion < destino):
            for x in range(loops):
                print(self.posicion)
                self.posicion += velocidad
            print(self.posicion)
            if (self.posicion != destino):
                self.posicion = destino
                print(self.posicion)
            
        else:
            print('ud ya se encuentra en esa posicion')
    
class Soldado(Personaje):
    
    def __init__(self,vida = 100, posicion = 0, velocidad=0, ataque=0):
        super().__init__(vida, posicion ,velocidad)
        self.ataque = ataque
    
    def atacar(self, personaje: Personaje):
        print('Atacando')
        personaje.recibir_ataque(self.ataque)


class Campesino(Personaje):
    def __init__(self,vida = 100, posicion = 0, velocidad=0, cosecha =0):
        super().__init__(vida, posicion ,velocidad)
        self.cosecha  = cosecha 
    
    def cosechar(self):
        print('La cantidad cosechada fue de '+ self.cosecha)
        return self.cosecha




s = Soldado()
c = Campesino()
s.mover(-9,1)
s.mover(10,2)
s.ataque = 70

s.atacar(c)
s.ataque = 40
s.atacar(c)

