'''
Este codigo nos enseña como declarar una funcion y luego llamarla 
para que sea ejecutado el codigo. Tiene varias funciones declaradas
y como utilizarlas con parametros y argumentos.
'''


def say_hello_empty():  # funcion sin parametros
    print('Hola Darien')


def say_hello(name, emoji):  # funcion con parametros
    print(f'Hola {name} {emoji}')


def say_hello_defaul(name='Darth Vader', emoji=';*|'):
    print(f'Hola {name} {emoji}')


say_hello_empty()
# argumentos que utilizados por los parametros, deben estar en el mismo orden.
say_hello('Darien Hdez', ';-)')

say_hello_defaul()  # utiliza los parametro establecidos por default
# utiliza el argumento Darien e utilizar el parametro del emoji por default
say_hello_defaul('Darien')
say_hello_defaul('Darien', ':-)')  # utiliza ambos argumentos escritos
