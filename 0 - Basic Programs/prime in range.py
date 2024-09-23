# Calculate prime numbers in range (x,y)
import math
def check_prime(n):
    on = int(math.sqrt(n))
    for i in range(2, on + 1 ):
        if n%i == 0:
            return "Not Prime"
    return "Prime"

def check_prime_range(x,y):
    for i in range(x,y+1):
        if check_prime(i) == "Prime":
            print(i, end=" ")
check_prime_range(4,89)

