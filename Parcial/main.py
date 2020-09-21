class Personaje():

    def __init__(self,nombre:str ,  vida=100, posicion=0, velocidad=0):
        self.nombre = nombre
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad

    def recibir_ataque(self, cantidad):
        if (cantidad < self.vida):
            self.vida -= cantidad
            print(self.nombre + ' recibio un ataque, su vida quedo en ' + str(self.vida))
        else:
            self.vida = 0
            print('el personaje ' + self.nombre + ' se quedo sin vida')

    def mover(self, destino):
        if (self.velocidad <= 0):
            return
        print(self.nombre +' esta moviendose desde ' + str(self.posicion) + ' hasta ' +
              str(destino) + ' con una velocidad de ' + str(self.velocidad))
        # implementar-----------------------------------------------------------------
        loops = int(abs((self.posicion-destino))/self.velocidad)
        if (self.posicion > destino):
            for _ in range(loops):
                print(self.posicion)
                self.posicion -= self.velocidad
            print(self.posicion)
            if (self.posicion != destino):
                self.posicion = destino
                print(self.posicion)
            print(self.nombre + ' llego a destino')

        elif(self.posicion < destino):
            for _ in range(loops):
                print(self.posicion)
                self.posicion += self.velocidad
            print(self.posicion)
            if (self.posicion != destino):
                self.posicion = destino
                print(self.posicion)
            print(self.nombre + ' llego a destino')

        else:
            print(self.nombre + ' ya se encuentra en esa posicion')


class Soldado(Personaje):

    def __init__(self,nombre:str, vida=100, posicion=0, velocidad=4, ataque=10):
        super().__init__(nombre,vida, posicion, velocidad)
        self.ataque = ataque

    def atacar(self, personaje: Personaje):
        print(self.nombre + 'esta atacando a :' +personaje.nombre)
        personaje.recibir_ataque(self.ataque)


class Campesino(Personaje):
    def __init__(self,nombre:str, vida=100, posicion=0, velocidad=2, cosecha=0):
        super().__init__(nombre,vida, posicion, velocidad)
        self.cosecha = cosecha

    def cosechar(self):
        print('La cantidad cosechada por ' + self.nombre + ' fue de ' + str(self.cosecha))
        return self.cosecha


print('---------------------------------------------------------')
print('El campesino puede moverse, cosechar y recibir un ataque')
c = Campesino('Campesino')
c.cosecha = 20
c.cosechar()
c.mover(9)
c.recibir_ataque(10)


print('---------------------------------------------------------')
print('El soldado puede moverse, atacar y recibir un ataque')
s1 = Soldado('Soldado 1')
s2 = Soldado('Soldado 2')

s1.mover(-9)
s1.mover(10)

s1.atacar(c)
s1.atacar(s2)
s1.recibir_ataque(110)
print('---------------------------------------------------------')