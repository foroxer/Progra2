#Realice un ejemplo en código donde se utilicen los métodos especiales init, new, del, str y cmp.
#el metodo cmp no existe en python3
class A(object):
    var = 123

    def __new__(cls):
        print("new")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("init")

    def __del__(self):
        print("del")

a = A()
print("string e la variable numerica : " + str(a.var))
del a