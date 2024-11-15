def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4== 0:
        if (year / 100)%2 !=0 and year%400 == 0:
            return True
            
    else: return False
    
print(is_)