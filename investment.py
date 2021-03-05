def calculate_apr(principal, interest_rate, years):
    """
    Calculates the interest rate with years
    """
    i=0
    output = 0
    for i in range(years):
        output = principal(1 + interest_rate)**(years)
    if principal < 0:
        print(bool(0))
    elif interest_rate < 0:
        print(bool(0))
    else:
        print(bool(0))
    print(output)
calculate_apr(principal, interest_rate, years)

