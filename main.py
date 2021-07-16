def math():
    # Funtion to find
    
    num1 = float(input('For what number you want to find multiplication table:- '))
    # Here you will enter the number for which you will find the multiplication table
    
    res1 = float(num1) * 1
    res2 = float(num1) * 2
    res3 = float(num1) * 3
    res4 = float(num1) * 4
    res5 = float(num1) * 5
    res6 = float(num1) * 6
    res7 = float(num1) * 7
    res8 = float(num1) * 8
    res9 = float(num1) * 9
    res10 = float(num1) * 10
    # Here your answer will be produced
    
    print(num1, 'X', '1', '=', res1)
    print(num1, 'X', '2', '=', res2)
    print(num1, 'X', '3', '=', res3)
    print(num1, 'X', '4', '=', res4)
    print(num1, 'X', '5', '=', res5)
    print(num1, 'X', '6', '=', res6)
    print(num1, 'X', '7', '=', res7)
    print(num1, 'X', '8', '=', res8)
    print(num1, 'X', '9', '=', res9)
    print(num1, 'X', '10', '=', res10)
    # This will print your answers
    
    quit = input('Press 1 to quit else rerun will be there:-')
    # Asking you to quit or not
    
    if quit == '1':
        print('Work Done! Now you can quit program')
    else:
        math()
    # Process to quit process or not
    
math()
# Command to run function
