#x=int(input('x: '))
#y=int(input('y: '))
#print(f' {x}/{y}={x/y}')
import sys

try:
    x=int(input('x: '))
    y=int(input('y: '))
except ValueError:
    print('Error de valor')
    sys.exit(1)

try:
    resultado=x/y
except ZeroDivisionError:
    print('Error al dividir por cero')
    sys.exit(1)
print(f' {x} / {y} = {resultado}')

