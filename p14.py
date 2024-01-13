           # 333
           # 313
           # 323
           # 333

row=4
for i in range(0,row):
    for j in range(1,row):
        if i==0 or i==row-1 or j==1 or j==row-1:
            print("3",end="")
        else:
            print(i,end="")
    print()

