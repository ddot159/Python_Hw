def calculator(number1, number2, operator):    
    """
    Calculator uses the following operators on numbers 1 and 2:
    
    addition (+),
    subtraction(-),
    multiplication(*)
    division(/),
    integer division (//)
    power(**) operation
 
    If the operator is invalid, the program exits
    """
    output = 0
    if operator == '+': 
        output = number1 + number2
        return float(output)  
	elif operator == '-':
        output = number1 - number2
        return float(output)
    elif operator == '*':
        output = number1 * number2
        return float(output)
    elif operator == '/':
        output = number1 / number2
        return float(output)
    elif operator == '//':
        output = number1 // number2
        return float(output)
    elif operator == '**':
        output = number1 ** number2
        return float(output)
    else: 
        return False #this condition makes it so that anything other than a string passes 
    


	
def input_output():
    '''
    Asks if the user wishes to continue, if not, the program exits
    '''
    i = 0 
    while i == 0: #this statement is for an infinite loop 
        
        input1 = input('Enter the first number: ')
        input2= input('enter the second number: ')
        operation = input('enter the operator: ')
        
        exit = ('Do you wish to exit? ')
        
        if exit == y
             break  #breaks the loop
        
        

                               
