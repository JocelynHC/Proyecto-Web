#Listas
nombre='Paulina'
print(nombre[0])
nombres=['Paulina' , 'Moises' , 'Hector' , 'Balam' , 'Raúl' , 'Jocelyn']
print(nombres)

nombres[0]='Max'
print(nombres)
nombres.sort()
print(nombres)

nombres.append('Paulina')
print(nombres)

nombres.reverse()
print(nombres)

#Tuplas
tupla= (1, 2, 3, 4, 5, 3, 5)

print(tupla)
print(tupla.count(3))
print(tupla.index(3))
#tupla[0=23]

#Conjuntos o set
s=set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)
s.remove(3)
print(s)
s.add(2)
print(s)

#Diccionarios
edades={'Paulina':21 , 'Moises':22 , 'Hector':23 , 'Balam':24 , 'Raúl':25 , 'Jocelyn':26}
colores={'rojo':255}
print(edades)
print(edades['Jocelyn'] )
print(colores['rojo'] )
edades['Raúl']=20
print(edades)
edades['Balam']+=1
print(edades)

#las listas(arreglos) son una secuencia de variables mutables(se pueden modificar)
#Las tuplas son una secuencia no mutables de variables
#Set o conjuntos son una coleccion de valores unicos
#diccionarios son una coleccion de valores que no son unicos pares de llave-valor

#Matrices
m= [ [1,2,3] , [4,5,6] ]
print(m)
print(m[0][2])
m=[[1],[2],[3]]
print(m)
print(m[-1])
