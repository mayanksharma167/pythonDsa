"""
A
B C
D E F
G H I J


ord('A') converts the character 'A' to its ASCII value (65).
chr(char) converts the ASCII value back to the corresponding character.
Each time, we increment the char value by 1 to get the next character in the alphabet.
"""

def char_pattern(n):
    char = ord('A')
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(char), end=" ")
            char = char+1
        print("\n")
char_pattern(4)
