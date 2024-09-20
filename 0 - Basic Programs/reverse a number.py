# Reverse a number

def reverse(n):
    rev = 0
    while n>0:
        last_digit = n%10
        rev = (rev*10) + last_digit
        n = n//10
    print(rev)
reverse(2387)