            # 3
            # 45
            # 678
            # 9101112
            # 678
            # 45
            # 3

ch=3
row=5
for  i in range(1,row+1):
    for j in range(i):
        print(ch,end="")
        ch+=1
    print()


for i in range(row,-1,-1):
    ch = ch // 2
    for j in range(1,i):
        print(ch,end="")
        ch+=1
    print()


