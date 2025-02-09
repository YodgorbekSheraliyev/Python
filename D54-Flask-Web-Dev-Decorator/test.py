# TODO: Create the logging_decorator() function 👇

# TODO: Use the decorator 👇

def logging_decorator(function):
    def wrapper(*args):
        function(args)
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)
    
# print(a_function(1,2,3))
def getArgs(*args):
    print(args)

getArgs(11,2,3,4)
# print(sum((1,3,4)))