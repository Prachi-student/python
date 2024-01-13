# *
# **
# ***
# ****
# ***
# **
# *
row=4

for i in range(row):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(row-1):
    for j in range(row-i-1):
        print("*",end="")
    print()