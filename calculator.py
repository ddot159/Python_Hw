def calculator(number1, number2, operator):
    """
    Calculator uses the following functions:
 
    addition (+),
    subtraction(-),
    multiplication(*)
    division(/),
    integer division (//)
    power(**) operation
 
    If the operator is invalid, the program exits
    """
    addition = '+'
    subtraction = '-'
    multiplication = '*'
    division = '/'
    integer_division = '//'
    power = '**'
    
    if operator == addition:
        print(number1 + number2)
    elif operator == subtraction:
        print(number1 - number2)
    elif operator == multiplication:
        print(number1 * number2)
    elif operator == division:
        print(number1 / number2)
    elif operator == integer_division:
        print(number1 // number2)
    elif operator == power:
        print(number1 ** number2)
    else: 
        print(bool(0))
    calculator(number1, number2, operator)
	
def input_output(x):
    '''
    Asks if the user wishes to continue, if not, the program exits
    '''
    print('do you wish to exit?')
    if x == 'y':
        calculator(number1, number2, operator)
    elif x == 'n':
        return
    print('do you wish to exit?')
    input_output(x)
                                
