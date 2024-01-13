        #    ****
        #   ****
        #  ****
        # ****


row=4
for i in range(row):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(row):
        print("*",end="")
    print()