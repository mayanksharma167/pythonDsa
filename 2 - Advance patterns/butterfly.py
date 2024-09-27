"""
*             *
* *         * *
* * *     * * *
* * * * * * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *

"""
def butterfly(n:int):
    # First half
    for i in range(1,n+1):
        #star 1
        for j in range(1, i+1):
            print("*",end=" ")
        #Space
        for j in range(1, 2*(n-i)+1):
            print(" ",end=" ")

        #star 2
        for j in range(1, i+1):
            print("*",end=" ")
        print()
    # Second half (Just change the outer loop to descending.)
    for i in range(n,0, -1):
            # star 1
        for j in range(1, i + 1):
            print("*", end=" ")
            # Space
        for j in range(1, 2 * (n - i) + 1):
            print(" ", end=" ")

            # star 2
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
butterfly(4)