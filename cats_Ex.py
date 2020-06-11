'''
Este codigo nombre tres gatos y luego nos dice el nombre y la edad del gato mas viejo,
y el nombre y la edad del gato mas joven utilizando Class y metodos dentro del Class.
'''


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Kitty', 2)
cat2 = Cat('Mitty', 4)
cat3 = Cat('Pitty', 5)
cat4 = Cat('Loki', 100)


def oldest_cat(*args):
    return max(args)


def young_cat(*args):
    return min(args)


print(
    f'The oldest cat is {oldest_cat(cat1.name, cat2.name, cat3.name)} and has {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
print(
    f"The youngest cat is {young_cat(cat1.name, cat2.name, cat3.name)} and has {young_cat(cat1.age, cat2.age, cat3.age)} years old.")
