# Error Handling

while True:
    try:
        age = int(input('What is your age?'))
        print(age)
    except ValueError:
        print('enter a number')
    # except ZeroDivisionError:
    #     print('enter a number greater than 0')
    
    else:
        print('Thank you')
        break
