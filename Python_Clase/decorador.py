def decora(f):
    def envuelve():
        print('Estoy a punto de ejecutar la función')
        print('Cobija')
        f()
        print('Termine de ejecutar la función')
        print('Sabana')
    return envuelve

@decora
def hola():
    print('Hola mundo!')
hola()