import time
def calculate_time(func):
    """
    this is a function to calculate how long it takes for the decorator to
    compute the time
    """
    def wrapper():
        time_earlier = time.time()
    return wrapper

@calculate_time
def time():
    time_now = time.time()
    print(time_now - time_earlier)
