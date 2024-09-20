"""
1
1 2
1 2 3
1 2 3 4

LOGIC:
1 - num of lines (4)
2 - num of line 1 -> (1),
    num of line 2 -> (1 , 2)
    .
    .
    .
    num of line n -> (1, 2, .....n)
"""

def half_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print("\n")
half_pyramid(4)

