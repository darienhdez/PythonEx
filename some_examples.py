from time import time
from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(string):
    return string.upper()


print(list(map(capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))

# Decorator


def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func()


@my_decorator
def hello():
    print('helloooo')


@my_decorator
def bye():
    print('see ya later')

# decorator2


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000):
        i*5


long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)




 