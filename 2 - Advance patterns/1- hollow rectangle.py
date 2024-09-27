"""
* * * * *
*       *
*       *
* * * * *

Hollow rectangle

>> check for boundary of the matrix
"""
def hollow_rectangle(row:int, columns:int):
    for i in range(1,row+1):
        for j in range(1,columns+1):
            if i == 1 or i == row or j == 1 or j == columns:
                print("* ",end="")
            else:
                print(" ",end=" ")
        print()

hollow_rectangle(6,18)
