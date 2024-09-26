"""
Inverted half puramid with numbers
12345
1234
123
12
1




"""

def inv_half_pyd_num(n):
    for i in range(1,n+1):
        for j in range(1, n-i+2):
            print(f"{j} ",end="")
        print()

inv_half_pyd_num(5)