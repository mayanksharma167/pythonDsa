"""
* * * *
* * *
* *
*

LOGIC:
1 - num of lines (4)
2 - num of line 1 -> (4  star),
    num of line 2 -> (3  star)
    .
    .
    .
    num of line n -> (1  star)
"""
def starInverted(n):
    for i in range(1,n+1):
        for j in range(n-i +1):
            print("*", end=" ")
        print("\n")
starInverted(4)