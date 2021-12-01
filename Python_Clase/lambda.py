libros = [
    {'Título':'El principito', 'Año':1943},
    {'Título':'El arte de la guerra', 'Año':1772},
    {'Título':'La ciudad de las bestias', 'Año':2002},
    {'Título':'El hobbit', 'Año':1984},
    {'Título':'La grieta', 'Año':2007},
]

#print(type(libros[0]))
#libros.sort() No podemos comparar objetos sin decir algo mas sobre ellos
#libros.sort(key='Año') sort no sabe que debe buscar dentro del diccionario


def ftitulo(libro):
    return libro['Título'].upper()

#print(ftitulo(libros[0]))

def faño(libro):
    return libro['Año']

#print(faño(libros[0]))

print(libros)
print()
#print('Libros ordenados por año:')
#libros.sort(key=faño)
#print(libros)


#print('Libros ordenados por título:')
#libros.sort(key=ftitulo)
#print(libros)

libros.sort(key=lambda libro:libro['Año'])
for libro in libros:
    #print(f" El libro  {libro['Título']} fue publicado en {libro['Año']}")
    print(' El libro  {Título} fue publicado en {Año}' .format(**libro) )
#print(libros)
libros.sort(key=lambda libro:libro['Título'])
#print(libros)