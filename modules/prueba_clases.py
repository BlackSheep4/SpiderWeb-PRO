class Perro:
    nombre = "Fido"
    edad = 2

    def ladrar(self):
        print("¡Guau! ¡Guau!")

# Crear un objeto de la clase Perro
mi_perro = Perro()

# Acceder a atributos y métodos del objeto
print(f"Nombre del perro: {mi_perro.nombre}")
print(f"Edad del perro: {mi_perro.edad}")
mi_perro.ladrar()

# Modificar atributos del objeto
mi_perro.nombre = "Max"
mi_perro.edad = 3

print(f"Nuevo nombre del perro: {mi_perro.nombre}")
print(f"Nueva edad del perro: {mi_perro.edad}")
