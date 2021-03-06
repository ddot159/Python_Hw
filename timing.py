import time
def calculate_time(func):
    """
    this is a function to calculate how long it takes for the decorator to
    compute the time
    """
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        print(f"Total time {int(y)-int(x)}")
    return wrapper

@calculate_time
def time_sleep():
      time.sleep(2)
time_sleep()     
