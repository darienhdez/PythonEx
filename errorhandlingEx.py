# Error Handling Ex

#IF YOU ENTER A NUMBER > 0 THEN:
    #  run the else code: Thank you
    #  run the finally code: ok im finally done!
    #  run the print code: can you hear me?
    #  go back to the beginning because the statements remains True

    #IF YOU ENTER A LETTER THEN:
    #  run except ValueError code: please enter a number
    #  run the finally code: ok im finally done!
    #  run the continue: go back to the beginning

    # IF YOU ENTER ZERO (0) THEN:
    #  run except ZeroDivisionError code: enter a number greater than 0
    #  run finally code: ok im finally done!
    #  run the break: exit the loop

while True:
    try:
        age = int(input('What is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('enter a number greater than 0')
        break
    else:
        print('Thank you')
    finally:
        print('ok im finally done!')
    print ('can you hear me?')

    


