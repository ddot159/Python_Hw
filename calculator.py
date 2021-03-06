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
    
    output = 0
    if operator == addition:
        output = number1 + number2
    elif operator == subtraction:
        output = number1 - number2
    elif operator == multiplication:
        output = number1 * number2
    elif operator == division:
        output =number1 / number2
    elif operator == integer_division:
        output = number1 // number2
    elif operator == power:
        output = number1 ** number2
    else: 
        return False
    print(float(output))


	
def input_output(x):
    '''
    Asks if the user wishes to continue, if not, the program exits
    '''
    print('do you wish to exit?')
    if x == 'y':
        return
    elif x == 'n':
        calculator(number1,number2,operation)
    else:
        print('do you wish to exit?')

                                
