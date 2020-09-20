#Realice un ejemplo en código donde se demuestre el encapsulamiento

class Encapsulamiento:
    
    def __init__(self,var = ""):
        self._var = var
    
    #encapsulamos la variable var y solo es accesible mediante el metodo getVar
    def getVar(self):
        return self._var

a = Encapsulamiento("variable encapsulada")

print(a.getVar())