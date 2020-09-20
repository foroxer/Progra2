#Realice un ejemplo en código que permita polimorfismo 

arr=[]
numerico= True

#dependiendo el booleano el array se puede completar tanto con valores numericos como con Strings
if(numerico):
    for i in range(1,6):
        arr.append(i)
else:
    for i in range(1,6):
        arr.append(str(i))

print(arr);