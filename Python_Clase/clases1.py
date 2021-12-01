class Vuelo:
    def __init__(self, capacidad):
        self.capacidad=capacidad
        self.pasajeros=[]
    def getDisponibles(self):
        return self.capacidad-len(self.pasajeros)
    def addPasajero(self, nombre):
        if self.getDisponibles():
           self.pasajeros.append(nombre)
           return True
        else:
           return False 



vuleo=Vuelo(3)
personas=['Paulina' , 'Moises' , 'Hector' , 'Balam' , 'Raúl' , 'Jocelyn']
for persona in personas:
    if vuleo. addPasajero(persona):
        print(f' Se agregó a {persona} al vuelo')
    else:
        print(f' No hay asientos disponibles para {persona}')


#print(vuleo.getDisponibles())
#print(vuleo.addPasajero('Max1'))
#print(vuleo.addPasajero('Max2'))
#print(vuleo.addPasajero('Max3'))
#print(vuleo.addPasajero('Max4'))

print(vuleo.getDisponibles())


