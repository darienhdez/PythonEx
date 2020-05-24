'''
Este codigo presenta un arbol de navidad al definir una funcion y como
podemos hacer que se repita el codigo sin tener que duplicar. Con tan 
solo escribir show_tree() (las veces que desees) el codigo se repetira.
'''

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_tree():
    for row in picture:
        for pixel in row:
            if pixel == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print('')


print('Christmas Tree')

show_tree()
