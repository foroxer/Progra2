#Realice un ejemplo en código para herencia simple y múltiple

class Cuadrupedo:
    def iam(self):
        return "Cuadrupedo"

class Canino:
    def iam(self):
        return "Canino"
    def morder(self):
        print ("mordiendo")

#La clase perro hereda los metodos y atributos de Canino y de Cuadrupedo
class Perro(Canino,Cuadrupedo):
    pass

#La clase Gato solo hereda metodos y atributos de Cuadrupedo 
class Gato(Cuadrupedo):
    pass

perro = Perro()
perro.morder()
print(perro.iam())

gato = Gato()
#gato no puede morder porque no hereda de canino
#gato.morder()
print(gato.iam())

