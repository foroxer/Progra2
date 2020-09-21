from models.auto import Auto
from models.puerta import Puerta

a1 = Auto("a1","gris")
p1 = Puerta("gris")
p2 = Puerta("gris")
p3 = Puerta("gris")

a1.puertas.append(p1)
a1.puertas.append(p2)
a1.puertas.append(p3)

print(a1.toString())

if ( True ) :
    hola = "juan"

if (hola == "juan"):
    print("lala")

del a1