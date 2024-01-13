 #    *
 #   **
 #  ***
 # ****
 #  ***
 #   **
 #    *

row=4
for i in range(row):
    for k in range(row-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(row-1):
    for k in range(i+2):
        print(" ",end="")
    for j in range(row-i-1):
        print("*",end="")
    print()
#
#
