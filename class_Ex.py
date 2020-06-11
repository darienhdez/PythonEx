'''
Este codigo nos enseña como definir el Class y las propiedades del mismo
'''


class PlayerCharacter:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def out(self):
        print(
            f'Hola {self.name} {self.lastname} sabemos que usted tiene {self.age} años!!')


player1 = PlayerCharacter('Darien', 'Hdez', 40)
player2 = PlayerCharacter('Adrien', 'Colon', 6)
player3 = PlayerCharacter('Mauricio', 'Hdez', 4)

player1.out()
player2.out()
player3.out()

print(player1.name, player1.lastname, player1.age)

print(player2.name, player2.lastname, player2.age)

print(player3.name, player3.lastname, player3.age)
