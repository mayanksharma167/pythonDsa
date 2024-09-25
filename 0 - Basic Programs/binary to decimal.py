"Binary to decimal conversion"

n = 111011
def bin_to_dec(n):
    count = 0
    num = 0
    while n>0:
        ld = n%10
        n = n//10
        num = num + ld*2**count
        count += 1
    return num

print(bin_to_dec(n))


