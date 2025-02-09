import time
current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function(*args, **kwargs):
        time.sleep(5)
        global current_time
        function(*args)
        after_time = time.time()
        return after_time - current_time
    # wrapper_function()
    return wrapper_function
        

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()

slow_function()