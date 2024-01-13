# 3
# 44
# 555
# 6666
# 555
# 44
# 3

row=4
ch=3
for i in range(row):
    for j in range(i+1):
        print(ch,end="")
    print();
    ch += 1
ch=ch-2
for i in range(row-1):
    for j in range(row-i-1):
        print(ch,end="")
    print()
    ch-=1



