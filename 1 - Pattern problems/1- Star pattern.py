"""
*
* *
* * *
* * * * *

LOGIC:
1 - num of lines (4)
2 - num of line 1 -> (1  star),
    num of line 2 -> (2  star)
    .
    .
    .
    num of line n -> (n  star)
"""

def starOne(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        print("\n")
starOne(4)

