# Error Handling

while True:
    try:
        age = int(input('What is your age?'))
        print(age)

    except:
        print('enter a number')
    else:
        print('Thank you')
        break
