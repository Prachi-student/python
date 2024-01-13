  #    *
  #  *   *
  # *     *
  # *******

row=4;
for i in range(row):
    for k in range(row-i-1):
        print(" ",end="")
    if i==0 or i==row-1:
        for j in range(0,i*2+1):
            print("*",end="")
    if i>0 and i<row-1:

        for j in range(0,i*2+1):
            if j==0 or j==(i*2+1)-1:
                print("*",end="")
            else:
                print(" ",end="")
    print()