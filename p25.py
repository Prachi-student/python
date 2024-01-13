# 3
# 4 5
# 6 7 8
# 9 10 11 12

k=3
row=4
for i in range(row):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()