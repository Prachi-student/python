           #    *
           #   ***
           #  *****
           # *******


n=int(input("enter rows..."))
for i in range(n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i*2+1):
        print("*",end="")
    print()
