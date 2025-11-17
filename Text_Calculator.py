#Calculator Program

try:
    #Prompt user for first input
    userinput1 = float (input('Enter the first number: '))

    #prompt for an operator ('+', '-', '*', or '/)
    useroperator = input('Enter the operator, (+, -, *, /): ')

    #prompt user for second input
    userinput2 = float (input('Enter the second number: '))

    #Calculate and display result for  input
    if useroperator == '+':
        print(f'{userinput1 + userinput2}')
    elif useroperator == '-':
        print (f'{userinput1 - userinput2}')
    elif useroperator == '*':
        print (f'{userinput1 * userinput2}')
    elif useroperator == '/':
        print(f'{userinput1 / userinput2}')
    else:
        print('Invalid operator.')

except ZeroDivisionError:
    print('You cannot divide by zero.')
except ValueError:
    print('Enter a valid number.')










