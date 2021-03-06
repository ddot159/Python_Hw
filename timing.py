import time
def calculate_time(func):
    """
    this is a function to calculate how long it takes for the decorator to
    compute the time
    """
    def wrapper():
        x = int(time.time())
        func()
        y = int(time.time())
        print('Total time {y-x}')
    return wrapper

@calculate_time
def test_time():
      time.sleep(2)
test_time()     
