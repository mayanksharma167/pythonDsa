#Conversion from decimal to binary

def decimal_to_binary(n):
    binary = ""
    while n>0:
        rem = n%2
        n = n//2
        binary = str(rem)+binary
    return binary

print(decimal_to_binary(4))