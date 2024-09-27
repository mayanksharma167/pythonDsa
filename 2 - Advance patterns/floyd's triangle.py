"""
1
2 3
4 5 6
7 8 9 10
"""

def floyd_triangle(n):
    count = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(count, end=" ")
            count += 1
        print()

floyd_triangle(5)


