           # *******
           #  *****
           #   ***
           #    *

row=4
for i in range(row,-1,-1):
    for k in range(row-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print()

