# print("Ab"*3)
import string


def flippingBits(n:int):
    # Write your code here
    bin_n = bin(n)[2:]
    bin_n = (32-len(bin_n))*"0" + bin_n
    swapped_n = "".join(["0" if ch=="1" else "1" for ch in bin_n]) 
    n_pow = len(swapped_n)-1
    result = 0
    for num in swapped_n:
        result += int(num) * pow(2, n_pow)
        n_pow -=1
    return result

print(flippingBits(9))



# def to_decimal(n: str):
#     result = 0
#     for index in range(len(n) - 1, 0, -1):
