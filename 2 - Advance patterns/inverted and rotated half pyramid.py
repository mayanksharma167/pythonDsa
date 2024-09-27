"""
inverted abd rotated half pyramid.

        *
      * *
    * * *
  * * * *

"""
def rotated_half_pyramid(n:int):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            #spaces
            print("  ",end="")
        for k in range(1,i+1):
            print("* ",end="")

        print()

rotated_half_pyramid(5)
