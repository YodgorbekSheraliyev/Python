def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def calculator():
    is_continue = True
    operators = ['+', '-', '*', '/']
    result = int(input("Enter the first number: \n"))
    while is_continue:
        print(operators)
        operator = input("Pick an operator \n")
        
        if operator == '+':
            number = int(input("Enter the number: \n"))
            result +=number
        elif operator == '-':
            number = int(input("Enter the number: \n"))
            result -=number
        elif operator == '*':
            number = int(input("Enter the number: \n"))
            result *=number
        elif operator == '/':
            number = int(input("Enter the number: \n"))
            result /=number
        else:
            print("Choose correct operator ")
            continue
        print(f"Result: {result}")
        should_continue = input("Will you do more operation? yer or no ").lower()
        
        if should_continue == "no":
            is_continue = False
            return result
    return result
            
            
        
print(calculator())