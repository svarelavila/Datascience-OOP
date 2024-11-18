from DiamondTrap import King
from S1E7 import Baratheon, Lannister
from S1E9 import Character, Stark

# Crear una instancia de Joffrey Baratheon
Joffrey = King("Joffrey")

# Imprimela informacion de Joffrey (doc y atributos)
print(Joffrey.__doc__)
print(Joffrey.__dict__)

# Usar set para cambiar atributos (ojos y pelo)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")

# Obtener e imprimir el color de ojos y pelo
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())

# Imprimir nuevamente el diccionario de atributos y métodos
print(Joffrey.__dict__)

