def calculate_apr(principal, interest_rate, years):
    """
    Calculates the interest rate with years
    """
    i= -1 #for the in range method I offset it by 1 to match the years value.
    output = 0
    
    if principal <= 0: #I did these if statements to check all 3 parameters.
        return False
    elif interest_rate <= 0:
        return False
    elif years <=0:
        return False
    else:
        for i in range(years):
            i = i + 1    
            output = principal*(1 + interest_rate)**years
            return float(output) 
   
