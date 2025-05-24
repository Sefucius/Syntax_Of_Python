sum=0
i=1
# 求1到100之间的偶数和
while i<=100:
    if i%2==1:
        i+=1
        continue
    sum+=i
    i+=1
print("1到100之间的偶数和为：",sum)

# 求1到100之间的奇数和
sum=0
for a in range(1,101):
    if a%2==0:
        continue
    sum+=a
print("1到100之间的奇数和为：",sum)