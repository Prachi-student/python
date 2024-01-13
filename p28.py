# 3-------1
# 54------2
# 876-----3
# 1211109---4
# 876
# 54
# 3


row=10
ch=3
c=3
for i in range(1,row+1):
    for j in range(1,i+1):
        print(ch,end="")
        ch-=1
        if((i==row-1)and(j==1)):
            temp=ch+1;
    print()
    ch=ch+c;
    c=c+2;



for i in range(row-1,-1,-1):
    for j in range(i):
        print(temp,end="")
        temp -= 1
    print()

