#3.Escriba en un mismo código de ejemplo las sentencias condicionales y 
# de iteración para cada estructura conocida del lenguaje: [if, elseif y else] [while y for].
lista=[1,2,3,4,5,6,7,8,9,0]

if(lista[0] == 0):
    print("la posicion 0 no es 0")
elif (lista[0] == 2):
    print("la posicion 0 no es 2")
else:
    print("la posicion 0 no es ni 0 ni 2")


vueltas = 10
while vueltas > 0:
    print(vueltas)
    vueltas -= 1

for var in lista:
    print(var)