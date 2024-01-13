# 2
# 34
# 567
# 891011
# 891011
# 567
# 34
# 2

row =4
ch=2
# for i in range(row):
#     for j in range(i+1):
#         print(ch,end="")
#         ch+=1
#     print()
ch=12
ch=ch-row
for i in range(row,-1,-1):
    for j in range(i):
        print(ch,end="")
        ch+=1
    print()
