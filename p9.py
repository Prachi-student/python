           # *
           # **
           # ***
           # ****
row=4
for i in range(row):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for j in range(0,i*2+1):
        print("*",end="")
    print()