import time
def calculate_time(func):
    """
    this is a function to calculate how long it takes for the decorator to
    compute the time
    """
    def wrapper():
        time_earlier = time.time()
        func()
        time_now = time.time()
        print('Total time'+ {int(time_now) - int(time_earlier)})
    return wrapper

@calculate_time
def time_sleep():
      time.sleep(2)
time_sleep()     
