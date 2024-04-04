#construtor de formatos (esfera, cilindro, retângulo (é em 3d então é paralelepípedo))
class Sphere:
    def __init__(self, radius):
        self.radius = radius

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

class Rectangle:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
pi = 3.14159265359 #fato engraçado



def volumeCalculator():
    print("a = esfera, b = cubo, c = cilindro;")
    shape = input("Insira o formato do recipiente: ")
    t = None
    #inicializa o formato de acordo com a entrada do usuário
    if shape == "a":
        t = Sphere(float(input("Insira o raio da esfera: ")))
    elif shape == "b":
        t = Rectangle(float(input("Insira o comprimento do prisma: ")), float(input("Insira a largura do prisma: ")), float(input("Insira a altura do prisma: ")))
    elif shape == "c":
        t = Cylinder(float(input("Insira o raio do cilindro: ")), float(input("Insira a altura do cilindro: ")))
    else:
        #repetir o prompt caso o usuário seja rebelde
        print ("Insira um formato válido.")
        volumeCalculator();
    if t != None:
        print(t)
    #mostrar o resultado
    print(calculateVolume(t))
        
def calculateVolume(t):
    v = None
    if type(t) == Sphere:
        v = (4 * pi * t.radius**3) / 3
    elif type(t) == Rectangle:
        v = t.length * t.width * t.height
    elif type(t) == Cylinder:
        v = pi * t.radius **2 * t.height
    else:
        v = 0
    return v

if __name__ == "__main__":
    volumeCalculator()
