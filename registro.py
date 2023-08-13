class Registro:
    def __init__(self, nombre, edad, identificacion):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"ID: {self.identificacion}")

registro1 = Registro("Ejemplo", 25, "12345")
registro1.mostrar_informacion()
