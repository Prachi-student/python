# 2
# 33
# 444
# 5555
# 5555
# 444
# 33
# 2

row=6
ch=2
for i in range(row):
    for j in range(i+1):
        print(ch,end="")
    print()
    ch+=1

ch-=1
for i in range(row,-1,-1):
    for j in range(i):
        print(ch,end="")
    print()
    ch-=1