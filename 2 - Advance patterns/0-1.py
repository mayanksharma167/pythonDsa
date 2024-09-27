"""
1
0 1
1 0 1
0 1 0 1

HINT: i+j == even ("1")
      i+j == odd  ("0")
"""
def zero_one(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            if (i+j)%2 == 0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
zero_one(5)