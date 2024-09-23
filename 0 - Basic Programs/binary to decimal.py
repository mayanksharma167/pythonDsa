"Binary to decimal conversion"

n = 1011
count = 0
num = 0
while n>0:
    ld = n%10
    n = n//10
    num = num + ld*2**count
    count += 1
print(num)


