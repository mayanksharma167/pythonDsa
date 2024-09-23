# program to check prime

# def check_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return "Not a Prime Number"
#         return "Prime Number"
#
# print(check_prime(127))

#Optimized version

import math
def check_prime(n):
    on = int(math.sqrt(n))
    for i in range(2, on + 1 ):
        if n%i == 0:
            return "Not a Prime Number"
        return "Prime Number"

print(check_prime(126))


