"""
A
B C
D E F
G H I J

"""

def char_pattern(n):
    char = ord('A')
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(char), end=" ")
            char = char+1
        print("\n")
char_pattern(4)