def calculate_apr(principal, interest_rate, years):
    """
    Calculates the interest rate with years
    """
    i=0
    output = 0
    for i in range(years):
        if i == years:
            output = principal*(1 + interest_rate)**(years)
        else:
            i += 1
    if principal < 0:
        return(bool(0))
    elif interest_rate < 0:
        return(bool(0))
    else:
        return(bool(0))
    print(output)

