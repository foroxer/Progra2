class Auto:
    marca = None
    
    def __init__(self,name, color):
        self.name = name 
        self.color = color
        self.puertas = []

    def toString(self):
        msg = ' Auto:{ name: ' + self.name + ', color: ' + self.color
        for p in self.puertas:
            msg += p.toString()
        msg = msg + '}'
        return (msg)

    